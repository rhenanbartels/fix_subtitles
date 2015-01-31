#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import argparse
import datetime
import re

#pattern to find time in subtitles
PATTERN = "\d{2}:\d{2}:\d{2},\d{3}"


def _open_file(file_name):

    #test file extension:.srt
    if file_name.endswith(".srt"):
        with open(file_name, "r") as file_object:
            file_content = file_object.read()
            file_content_list = file_content.split("\r\n")
            return file_content_list
    else:
        raise IOError("File must have .srt extension!")

def _synch_subtitle(file_content):
    #Get the seconds of subtitle time: xx:xx:20,xxx
    time_splited= file_content.split("-->")
    return [time_values.strip() for time_values in time_splited]

def _add_miliseconds(subtitle_time, offset):
    subtitle_with_offset = []
    for sub_time in subtitle_time:
        subtitle_datetime = datetime.datetime.strptime(sub_time, "%H:%M:%S,%f")
        subtitle_datetime += datetime.timedelta(seconds=offset / 1000.0)
        date_time = subtitle_datetime.time()
        #Add the offset to subtitle time.
        hour_str = date_time.hour if len(str(date_time.hour)) != 1 else "0" +\
            str(date_time.hour)
        minute_str = date_time.minute if len(str(date_time.minute)) != 1 else \
                "0" + str(date_time.minute)
        second_str = date_time.second if len(str(date_time.second)) != 1 else \
                "0" + str(date_time.second)
        microsecond_str = "{:.3}".format(str(date_time.microsecond))
        subtitle_with_offset.append("{hour}:{min}:{sec},{milisec}".\
                format(hour=hour_str, min=minute_str, sec=second_str,
                       milisec=microsecond_str))

    return subtitle_with_offset

def _rebuild_subtitle_time(subtitle_with_offset):
    subtitle_rebuilded = "{init} --> {final}".\
            format(init=subtitle_with_offset[0], final=subtitle_with_offset[1])
    return subtitle_rebuilded

def _check_subtitle_time_pattern(subtitle_time):
    if re.match(PATTERN, subtitle_time):
        return True
    else:
        return False

def main():
    #Command line arguments: filename and offset.
    parser = argparse.ArgumentParser()
    parser.add_argument('--file','-f', required=True, type=str, help=
            'Subtitle filename to sync')
    parser.add_argument('--offset','-o', required=True, type=int, help=
            'Deslocation of subtitle in miliseconds (ms)')
    args = parser.parse_args()
    file_name = args.file
    offset = args.offset

    file_content = _open_file(file_name)
    if file_content is not None:
        final_file_name = "fixed_" + file_name
        with open(final_file_name, "w") as fobj:
            for lines in file_content:
                if _check_subtitle_time_pattern(lines):
                    subtitle_time = _synch_subtitle(lines)
                    subtitle_with_offset = _add_miliseconds(subtitle_time,
                                                            offset)
                    final_subtile_time =\
                            _rebuild_subtitle_time(subtitle_with_offset)
                    fobj.write(final_subtile_time + "\r\n")
                else:
                    fobj.write(lines + "\r\n")

    else:
        raise IOError("Something went wrong! Please check your file!")

if __name__ == "__main__":
    main()
