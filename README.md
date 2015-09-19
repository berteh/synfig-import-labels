# Import Audacity Labels as Keyframes and/or Kinetic Typography (artistic subtitles)

A [Synfig](http://synfig.org) plug-in to create time reference and/or artistic kinetic text effects in Synfig, from [Audacity](http://audacity.sourceforge.net/) track labels (aka subtitles).

Synfig Studio is a free and open-source 2D animation software, designed as powerful industrial-strength solution for creating film-quality animation using a vector and bitmap artwork.

The generated time reference (keyframes) is great for synchronizing animation with your audio.

The generated kinetic texts objects is a great basis for beautiful typographic animations, and can be customized easily to achieve your prefered effect(s).

## Gallery

Different Effects are readily available, and it is easy to create new ones:

**popping text**
<a href="test/popping-text_result.gif" target="_blank"><img src="test/popping-text_result.gif" alt="popping text" style="width: 30%; margin: 0px 1%;"></a>

**revealing text**
<a href="test/revealing-text_result.gif" target="_blank"><img src="test/revealing-text_result.gif" alt="revealing text" style="width: 30%; margin: 0px 1%;"></a>

**descending text**
<a href="test/descending-text_result.gif" target="_blank"><img src="test/descending-text_result.gif" alt="descending text" style="width: 30%; margin: 0px 1%;"></a></p>

got other ideas or templates? add them to the wiki or do a code pull request to share them!

Using a simple white background and importing a set of 6 text lines with their timings the following animation is generated automatically: automatic keyframes (top-right), automatic objects (bottom-right) auto-animated (bottom-left)
![example in synfig](http://i61.tinypic.com/fa1x3.jpg)

## Use
from the command-line: (only on sif files, unzip sifz manually before)

    python import-audacity-labels-keyframes.py in.sif (labels.txt (out.sif))

or from within synfig:   

1. open your synfig project, save it as .sif (Synfig Plug-ins don't work on the default .sifz format for now)
1. run the plugin at _> Plug-Ins > Import Audacity Labels as Keyframes_

to create your own timed labels file you can:

1. use [Audacity to label track segments](http://multimedia.journalism.berkeley.edu/tutorials/audacity/adding-labels/)
1. export your labels via Tracks > Edit Labels > export, in Audacity.

or simply use Excel/Calc and create a table with 3 columns: ``start time (in sec) - end time (in sec) - text (single line)`` and export as tsv (csv with ``tab`` separator), and rename it into ``labels.txt``. Not titles on the column, just the data, a bit like:

| 0.5 | 1.5 | first sentence showing for 1 second |
| 1.5 | 1.9 | cool ! |
| 2.4 | 3.2784 | your imagination is the limit ! |


## Video Tutorial

The use of this plugin to generate keyframes in a complete animation design is described in the [Synfig Audio Synchronisation tutorial](http://wiki.synfig.org/wiki/Doc:Audio_Synchronisation)

A tutorial will be written on creating kynetic typographies one day... but I (not secretly) hope you beat me to it!

## Install

Decompress [plugin archive](https://github.com/berteh/import-audacity-labels-keyframes/archive/master.zip ) into your synfig plugins directory (in linux: home/-user-/.synfig/plugins)

Another option is to clone [this repository](https://github.com/berteh/import-audacity-labels-keyframes.git) in the same location.

Requirements: Python (Synfig is a recommended option) - more info on [Synfig Plugins page](http://wiki.synfig.org/wiki/Doc:Plugins#How_to_install_plugins)

## Configuration

edit `settings.py` for customisation:

    # configuration for keyframes import
    #
    AUDACITY_LABELS_FILE = "labels2.txt" # audacity labels file name, must be located in your synfig project directory
    IMPORT_START = True                 # set to True to import keyframe for start of label
    IMPORT_END = True                   # set to True to import keyframe for end of label
    START_SUFFIX = ""                   # suffix to add to a label-start keyframe, to distinguish it from label-end frame
    END_SUFFIX = " - end"               # suffix to add to a label-end keyframe, to distinguish it from label-start frame
    OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False   # set to True to replace keyframe with exact same description
    GENERATE_OBJECTS = True             # set to True to generate objects (such as text layers) for each label
    #
    # settings below only matter to object generation. don't bother if GENERATE_OBJECTS is False.
    TEMPLATE_NAME = "popping-text"  # the name of template you want to use. must be located in templates/ subdirectory, with .xml extension. default is "popping-text"
    ANIMATION_INTERVAL = 0.3        # interval (before and after the label time) used for transition, in seconds. default is 0.5
    RANDOM_ORIGIN = 70              # set to a percentage [0-100] to randomize the object origin in the whole document viewbox (0 will stack them all at [0,0])
    WAYPOINT_TYPE = "halt"          # one of: constant, auto, linear, clamped, halt
    VALUE_BEFORE = "0.0"
    VALUE_MIDDLE = "1.0"
    VALUE_AFTER = "0.3"

## Support
Preferably use github's [issues tracker](https://github.com/berteh/import-audacity-labels-keyframes/issues) for bug reports, feature requests and contributing to this code.
