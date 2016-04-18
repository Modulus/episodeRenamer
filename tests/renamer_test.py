import unittest
from code import renamer


class RenameTest(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(renamer.rename(None, None, None))

    def test_has_name(self):
        text = "03.01 - Conquest of Cuteness.mp4"
        expected = "S03E01 - Conquest of Cuteness.mp4"
        result = renamer.rename(text,  r"(\d+)(.*)(\d+)", ".")
        self.assertEqual(result, expected)

    def test_has_e(self):
        text = "06e12 - Ocarina.mp4"
        expected = "S06E12 - Ocarina.mp4"
        result = renamer.rename(text, r"(\d+)(\w*)(\d+)", "e")
        self.assertEqual(result, expected)
