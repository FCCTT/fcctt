#! /usr/bin/env python

"Walk through a directory to convert all the pictures."

import fnmatch
import os
 
rootPath = '/Users/oppih/Documents/FC2EPUB/issue56'
pattern0 = '*.jpg'
pattern1 = '*.png'

def walkThrough():
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern0):
            print os.path.join(root, filename).replace(' ', '_') # this produces a string
        for filename in fnmatch.filter(files, pattern1):
            #print os.path.join(root, filename)
            #convertPic(os.path.join(root, filename))
            print os.path.join(root, filename).replace(' ', '_') # this produces a string

def convertPic(picPathStr):
    # use ImageMagic tool to convert the size and file pattern
    pass


if __name__ == "__main__":
    walkThrough()