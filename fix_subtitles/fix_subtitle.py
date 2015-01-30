#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import argparse
import re

#pattern to find time in subtitles
pattern = "\d{2}:\d{2}:\d{2},\d{3}"


def _open_file(file_name):

    #test file extension:.srt
    if file_name.endswith(".srt"):
        with open(file_name, "r") as file_object:
            file_content = file_object.read()
            file_content_list = file_content.split("\r\n")
            return file_content_list
    else:
        raise IOError("File must have .srt extension!")

if __name__ == "__main__":
    #Command line arguments: filename and offset.
    parser = argparse.ArgumentParser()
    parser.add_argument('--file','-f', required=True, type=str, help=
            'Subtitle filename to sync')
    parser.add_argument('--offset','-o', required=True, type=int, help=
            'Deslocation of subtitle in miliseconds (ms)')
    args = parser.parse_args()
    file_name = args.file

    x =  _open_file(file_name)
    print x

