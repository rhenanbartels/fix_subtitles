import argparse
import unittest

from fix_subtitle import _add_miliseconds
from fix_subtitle import _open_file
from fix_subtitle import _rebuild_subtitle_time
from fix_subtitle import _synch_subtitle

class TestFixSubtitle(unittest.TestCase):
    def test_file_extension(self):
        file_name = "test.txt"
        self.assertRaises(IOError, _open_file, file_name)

    def test_file_in_list(self):
        file_name = "requiem.srt"
        with open(file_name, "r") as fobj:
            file_first_line = fobj.readline()

        self.assertEqual(_open_file(file_name)[0],
                 file_first_line.strip())

    def test_synch_subtitle(self):
        seconds = ["00:01:12,123", "00:11:32,456"]
        subtitle_time = "00:01:12,123 --> 00:11:32,456"
        self.assertEquals(_synch_subtitle(subtitle_time), seconds)

    def test_time_offset(self):
        answer = ["00:01:32,124", "00:01:34,134"]
        subtitle_time = ["00:01:31,000", "00:01:33,010"]
        self.assertEqual(_add_miliseconds(subtitle_time, 1124), answer)

    def test_subtitle_rebuild(self):
        subtitle_with_offset = ["00:12:13,123", "01:23:32,124"]
        result = "00:12:13,123 --> 01:23:32,124"
        self.assertEquals(_rebuild_subtitle_time(subtitle_with_offset), result)

