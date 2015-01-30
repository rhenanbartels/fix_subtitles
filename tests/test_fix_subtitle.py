import argparse
import unittest

from fix_subtitle import _open_file


class TestFixSubtitle(unittest.TestCase):
    def test_open_file(self):
        file_name = "requiem.srt"
        with open(file_name, "r") as fobj:
            file_first_line = fobj.readline()

        self.assertEquals(_open_file(file_name)[0], file_first_line.strip())


