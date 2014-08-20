# Import Audacity Labels as Keyframes

A [Synfig](http://synfig.org) plug-in to import [Audacity](http://audacity.sourceforge.net/) track labels as Synfig keyframes.

Synfig Studio is a free and open-source 2D animation software, designed as powerful industrial-strength solution for creating film-quality animation using a vector and bitmap artwork.

## Use
1. use [Audacity to label track segments](http://multimedia.journalism.berkeley.edu/tutorials/audacity/adding-labels/)
1. export your labels via Tracks > Edit Labels > export, in Audacity.
1. open your synfig project, save it as .sif (Synfig Plug-ins don't work on the default .sifz format for now)
1. run the plugin at _> Plug-Ins > Import Audacity Labels as Keyframes_

or use the command-line: (only on sif files, unzip sifz manually before)

    python import-audacity-labels-keyframes.py in.sif (labels.txt (out.sif))
    

The use of this plugin in a complete animation design is described in the [Synfig Audio Synchronisation tutorial](http://wiki.synfig.org/wiki/Doc:Audio_Synchronisation)

## Install

Decompress [plugin archive](https://github.com/berteh/import-audacity-labels-keyframes/archive/master.zip ) into your synfig plugins directory (in linux: home/-user-/.synfig/plugins)

Another option is to clone [this repository](https://github.com/berteh/import-audacity-labels-keyframes.git) in the same location.

Requirements: Python (Synfig is a recommended option) - more info on [Synfig Plugins page](http://wiki.synfig.org/wiki/Doc:Plugins#How_to_install_plugins)

## Configuration

edit `settings.py` for customisation:

    AUDACITY_LABELS_FILE = "labels.txt" # audacity labels file name, must be located in your synfig project directory
    IMPORT_START = True					# set to True to import keyframe for start of label
    IMPORT_END = False					# set to True to import keyframe for end of label
    START_SUFFIX = ""					# suffix to add to a label-start keyframe, to distinguish it from label-end frame
    END_SUFFIX = " - end"				# suffix to add to a label-end keyframe, to distinguish it from label-start frame
    OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False # set to True to replace keyframe with exact same description

## Support
Preferably use github's issues tracking system for bug reports, feature requests and contributing to this code.
