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
