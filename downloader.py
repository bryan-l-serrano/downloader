#!/usr/bin/env python
"""
you must have ffmpeg and youtube-dl (for python 2.7)
installed in order to run this
"""

import os
import sys

if len(sys.argv) > 1:
	url = sys.argv[1]
else:
	url = raw_input('Please Enter youtube URL')

os.chdir('Music')
os.system('youtube-dl --extract-audio --audio-format mp3 '+ url +'')
os.chdir('..')

    


            
