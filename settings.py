# configuration for keyframes import
#
AUDACITY_LABELS_FILE = "labels.txt" # audacity labels file name, must be located in your synfig project directory - TODO get filename from synfig filechooser or drag-n-drop: HOW?
IMPORT_START = True					# set to True to import keyframe for start of label
IMPORT_END = False					# set to True to import keyframe for end of label
START_SUFFIX = ""					# suffix to add to a label-start keyframe, to distinguish it from label-end frame
END_SUFFIX = " - end"				# suffix to add to a label-end keyframe, to distinguish it from label-start frame
OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False # set to True to replace keyframe with exact same description