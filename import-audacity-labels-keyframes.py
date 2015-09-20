#!/usr/bin/env python
#
# Copyright (c) 2014 by Berteh <berteh@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#------------------------------------------------
#
# usage
#
# from command line (only on sif files, need to unzip sifz manually)
#      python import-audacity-labels-keyframes.py in.sif (labels.txt (out.sif))
#
# from synfigstudio (only on sif files, need to save as sif in synfig first)
#      caret/right-click > Plug-Ins > Import Audacity Labels as Keyframes
#
#------------------------------------------------
# installation: see http://wiki.synfig.org/wiki/Doc:Plugins
# 
# decompress plugin archive into home/<user>/.synfig/plugins
#------------------------------------------------
#
# configuration is done by editing settings.py, the following options are available:
#
# AUDACITY_LABELS_FILE = "labels.txt" # audacity labels file name, must be located in your synfig project directory - TODO get filename from synfig filechooser or drag-n-drop: HOW?
# IMPORT_START = True				# set to True to import keyframe for start of label
# IMPORT_END = False				# set to True to import keyframe for end of label
# START_SUFFIX = ""					# suffix to add to a label-start keyframe, to distinguish it from label-end frame
# END_SUFFIX = " - end"				# suffix to add to a label-end keyframe, to distinguish it from label-start frame
# OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False # set to True to replace keyframe with exact same description
#
#------------------------------------------------
# Feel free to improve the code below and share your modifications at
# https://github.com/berteh/import-audacity-labels-keyframes/issues

import os
import sys
import xml.etree.ElementTree as ET
import re
import settings as s
import random
#import pystache  # only imported below if s.GENERATE_OBJECTS is True.

def secFrames2sec(fps, secFrame): #convert Synfig "Xs Yf" time notation to <float>s in seconds.
	pattern  = "^((\d+)s)?(\s)?((\d+)f)?$"
	m = re.match(pattern, secFrame)
	[ g1, sec, g2, g3, frame] = m.groups(0)
	return float(sec) + float(frame)/fps

def process(sifin_filename, labels_filename, sifout_filename):	

	#read audacity labels file
	if not os.path.exists(labels_filename):
		sys.exit("Audacity Labels file not found: %s " % labels_filename)
	with open(labels_filename, 'r') as f:
		#if s.DEBUG: print " reading labels from %s" % labels_filename # commented for "print" statements lead to syntax error in synfig.
		# Read the file contents and generate a list with each line
		lines = f.readlines()

	# read input sif file as xml
	tree = ET.parse(sifin_filename)
	canvas = tree.getroot()
	fps = int(float(canvas.get("fps")))
	
	# put existing keyframes description in attributes, to enable fast xpath search with no other external module
	for key in canvas.findall("./keyframe"):
		if key.text is not None :
			key.set("desc",key.text)
	#if s.DEBUG: 
	#	print " copied descriptions of keyframes to attributes in sif file:"
	#	ET.dump(canvas)

	#process labels into keyframes		
	pattern  = '(\d+)[,|\.](\d+)\t(\d+)[,|\.](\d+)\t(.+)$'
	texts = []
	starts = []
	ends = []
	
	for line in lines:
		# pattern applied to each line. 'match' is quite strict and starts at beginning of line, 'search' could be used instead for more flexibility (&risk) 
		m = re.match(pattern, line)
		if m:
			#convert audacity time to synfig seconds+frame.
			start = float(m.group(1)+"."+m.group(2))
			ss = int(start)
			sf = int(fps * (start - ss))

			end = float(m.group(3)+"."+m.group(4))
			es = int(end)
			ef = int(fps * (end - es))

			desc = str(m.group(5))

			
			#what follows is reusable for any format, TODO turn into function
			if s.IMPORT_START:
				k = canvas.find("keyframe[@desc='%s%s']" % (desc, s.START_SUFFIX))
				if s.OVERWRITE_KEYFRAMES_WITH_SAME_NAME or (k is None):
					if (k is None):
						#if s.DEBUG: print " creating keyframe: %s" % desc
						k = ET.Element('keyframe',{"active": "true"})				
						k.text = desc+s.START_SUFFIX
						canvas.append(k)

					k.set("time", "%ds %df" % (ss, sf)) #length is set automatically by synfig
				#elif s.DEBUG: print " skipping existing start keyframe: %s" % desc
			
			if s.IMPORT_END and not (start == end):
				k = canvas.find("keyframe[@desc='%s%s']" % (desc, s.END_SUFFIX))
				if s.OVERWRITE_KEYFRAMES_WITH_SAME_NAME or (k is None):
					if (k is None):
						#if s.DEBUG: print " creating keyframe: %s" % desc
						k = ET.Element('keyframe',{"active": "true"})				
						k.text = desc+s.END_SUFFIX
						canvas.append(k)

					k.set("time", "%ds %df" % (es, ef))
				#elif s.DEBUG: print " skipping existing end keyframe: %s" % desc

			if s.GENERATE_OBJECTS:
				texts.append(desc)
				starts.append(start)
				ends.append(end)

	# generate objects
	if s.GENERATE_OBJECTS:
		try:
			import pystache
			renderer = pystache.Renderer(search_dirs="templates", file_extension="xml") #todo preferably parse template only once before loop.

		except ImportError:
			#print "Could not load template engine for objects generation. Please verify you have both a pystache and templates subdirectories, or re-download & re-install this plugin."
			sys.exit() # skip objects generation
		
		b = secFrames2sec(fps, canvas.get("begin-time")) # lower bound for time
		e = secFrames2sec(fps, canvas.get("end-time")) # upper bound for time
		d = s.ANIMATION_INTERVAL
		r = s.RANDOM_ORIGIN
		z = 999934569.1341 # basis for groupid generation, any float > 0 would do.
		view = canvas.get("view-box").split()		
		[minx, maxy, maxx, miny] = [float(elem) for elem in view]

		for i,t in enumerate(texts):

			if s.SPLIT_WORDS:
				objects = t.split() # opt add separator as argument, space by default.
				objC = len(objects)
				objTimes = [starts[i] + (ends[i]-starts[i]) * j for j,word in enumerate(objects)]
			else:
				objects = [t]
				objTimes = [starts[i]]

			#generate object, turn into function
			for j,o in enumerate(objects):
				if (r>0):
					ox = random.uniform(minx, maxx)*r/100
					oy = random.uniform(miny, maxy)*r/100
				else:
					ox = 0
					oy = 0

				t1 = max(b,starts[i]-d)
				t2 = objTimes[j]
				t3 = ends[i]
				t4 = min(ends[i]+d,e)

				values = {
					'text':o,
					'value_before':s.VALUE_BEFORE,
					'value_after':s.VALUE_AFTER,
					'loop_before':s.LOOP_BEFORE,
					'loop_middle':s.LOOP_MIDDLE,
					'loop_after':s.LOOP_AFTER,
					'time1':str(t1)+'s',
					'time2':str(t2)+'s',
					'time3':str(t3)+'s',
					'time4':str(t4)+'s',
					'transition':s.WAYPOINT_TYPE,
					'origin_x':ox,
					'origin_y':oy
				}
				values.update({
					'group1':(z+t1).hex()[4:-4],
					'group2':(z+t2).hex()[4:-4],
					'group3':(z+t3).hex()[4:-4],
					'group4':(z+t4).hex()[4:-4]
					})
			
				#print "1 object is being added to canvas for '%s'"%t
				l = renderer.render_name(s.TEMPLATE_NAME, values)
				layer = ET.fromstring(l)
				canvas.append(layer)	

	# write modified xml tree to the same sif file
	tree.write(sifout_filename, encoding="UTF-8", xml_declaration=True)
	#if s.DEBUG: print "done"


#main
if len(sys.argv) < 2:
	sys.exit("Missing synfig filename as argument")
else:
	# defaults
	sifin_filename = sys.argv[1]
	#make sure the plugin is called on sif, and not sifz
	if not (os.path.splitext(sifin_filename)[-2].lower().endswith('.sif') or os.path.splitext(sifin_filename)[-1].lower().endswith('.sif')):
		sys.exit("Synfig plug-ins only work on sif file, not sifz.\n\nPlease save your Synfig project (%s) as sif, then try again." % sifin_filename)
	labels_filename = sys.argv[2] if len(sys.argv)>2 else os.path.join(os.path.dirname(sifin_filename), s.AUDACITY_LABELS_FILE)
	sifout_filename = sys.argv[3] if len(sys.argv)>3 else sifin_filename
	process(sifin_filename, labels_filename, sifout_filename)