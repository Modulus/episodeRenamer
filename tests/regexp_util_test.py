from code import regexp_util as rx
import unittest


class RegExpUtilTest(unittest.TestCase):

    def test_extract(self):
        text = "03.02 - Holy Cows on a blanket"
        expected = "03.02"
        result = rx.extract(text, r"(\d+)(.*)(\d+)")
        self.assertEqual(expected, result)



