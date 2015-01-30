import unittest
from fix_subtitle import _open_file
from fix_subtitle import _get_file_list


class TestFixSubtitle(unittest.TestCase):
    def test_file_extension(self):
        file_name = "test.txt"
        self.assertRaises(IOError, _open_file, file_name)
    def test_file_in_list(self):
        file_list = "00:01:32,234 --> 00:01:55,134\n"
        self.assertEqual(_get_file_list(_open_file("test.srt"))[0], file_list)


