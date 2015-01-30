#!usr/bin/env python
# -*- encoding:utf-8 -*-

import argparse
import re

#pattern to find time in subtitles
pattern = "\d{2}:\d{2}:\d{2},\d{3}"


def _open_file(file_name):
    #text file extension.
    if file_name.endswith(".srt"):
        with open(file_name, "r") as file_object:
            file_content = file_object.read()
            return file_content
    else:
        raise IOError:
            print "File extension must be .srt"

def _get_file_list(file_content):
    #break file in to lines
    file_content = _open_file("test.txt").split("\r\n")
    first_line = file_content
    return first_line



