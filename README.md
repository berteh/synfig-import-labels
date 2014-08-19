# Import Audacity Labels as Keyframes

A [Synfig](http://synfig.org) plug-in to import [Audacity](http://audacity.sourceforge.net/) track labels as Synfig keyframes.

Synfig Studio is a free and open-source 2D animation software, designed as powerful industrial-strength solution for creating film-quality animation using a vector and bitmap artwork.

## Install
Requirements: Python (Synfig is a recommended option)

Decompress plugin archive into your synfig plugins directory (in linux: home/<user>/.synfig/plugins)

Moreover at http://wiki.synfig.org/wiki/Doc:Plugins#How_to_install_plugins

## Use

from synfigstudio run the plugin at _> Plug-Ins > Import Audacity Labels as Keyframes_
   
from the command-line: (only on sif files, need to unzip sifz manually)

    python import-audacity-labels-keyframes.py in.sif (labels.txt (out.sif))

More: 

- how to use [Audacity to label track segments](http://multimedia.journalism.berkeley.edu/tutorials/audacity/adding-labels/)
- export your labels via Tracks > Edit Labels > export, in Audacity.

## Configuration

edit the plugin file directly for customisation:

    AUDACITY_LABELS_FILE = "labels.txt" # audacity labels file name, must be located in your synfig project directory
    IMPORT_START = True					# set to True to import keyframe for start of label
    IMPORT_END = True					# set to True to import keyframe for end of label
    START_SUFFIX = ""					# suffix to add to a label-start keyframe, to distinguish it from label-end frame
    END_SUFFIX = " - end"				# suffix to add to a label-end keyframe, to distinguish it from label-start frame
    OVERWRITE_KEYFRAMES_WITH_SAME_NAME = False # set to True to replace keyframe with exact same description


## Support
Preferably use github's issues tracking system for bug reports, feature requests and contributing to this code.
