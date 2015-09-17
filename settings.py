# configuration for keyframes import
#
AUDACITY_LABELS_FILE = "labels.txt" # audacity labels file name, must be located in your synfig project directory - TODO get filename from synfig filechooser or drag-n-drop: HOW?
IMPORT_START = True					# set to True to import keyframe for start of label
IMPORT_END = False					# set to True to import keyframe for end of label
START_SUFFIX = ""					# suffix to add to a label-start keyframe, to distinguish it from label-end frame
END_SUFFIX = " - end"				# suffix to add to a label-end keyframe, to distinguish it from label-start frame
OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False   # set to True to replace keyframe with exact same description
GENERATE_OBJECTS = True				# set to True to generate objects (such as text layers) for each label
#
# settings below only matter to object generation. don't bother if GENERATE_OBJECTS is False.
TEMPLATE_NAME = "simple-text"	# the name of template you want to use. must be located in templates/ subdirectory, with .xml extension. default is "simple-text"
ANIMATION_INTERVAL = 2			# interval (before and after the label time) used for transition, in number of labels (not in seconds)
RANDOM_ORIGIN = 50			    # set to a percentage [0-100] to randomize the object origin in the whole document viewbox (0 will stack them all at [0,0])