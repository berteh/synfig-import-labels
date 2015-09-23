# configuration for keyframes import
#
LABELS_FILE = "labels.txt" 	# audacity labels file name, must be located in your synfig project directory
IMPORT_START = True         # set to True to import keyframe for start of label
IMPORT_END = False           # set to True to import keyframe for end of label
START_SUFFIX = ""           # suffix to add to a label-start keyframe, to distinguish it from label-end frame
END_SUFFIX = " - end"       # suffix to add to a label-end keyframe, to distinguish it from label-start frame
OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False   # set to True to replace keyframe with exact same description
GENERATE_OBJECTS = True     # set to True to generate objects (such as text layers) for each label
#
# settings below only matter to object generation. don't bother if GENERATE_OBJECTS is False.
TEMPLATE_NAME = "appearing-text"  # the name of template you want to use. must be located in templates/ subdirectory, with .xml extension. default is "popping-text"
SPLIT_WORDS = False			# split each word in a separate object
WAYPOINT_TYPE = "halt"      # one of: constant, auto, linear, clamped, halt
RANDOM_ORIGIN = 70          # set to a percentage [0-100] to randomize the object origin in the whole document viewbox (0 will stack them all at [0,0])
ANIMATION_INTERVAL = 0.5    # interval (before and after the label time) used for (in & out) transition, in seconds. default is 0.5
#
####################
#
# changing the values behind this point is not recommended as it may break the examples provided in the templates/ directory...
# but if you still do, then you know what you're doing ;)
#
# values for "loop" based transitions (appearing,...)
LOOP_BEFORE = "0.0"
LOOP_MIDDLE = "1.0"
LOOP_AFTER = "0.3"
# values for "progressions" transitions (descending, revealing, fromleft...)
VALUE_BEFORE = "-1.0"
VALUE_MIDDLE = "0.0"
VALUE_AFTER = "1.0"
# location for plugin templates
TEMPLATE_DIR = "templates"
# labels parsing
TSV_SEPARATOR = "\t" # single character separating data fields in LABELS_FILE
HEADER = ["start","stop","text","template"]