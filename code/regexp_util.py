import re


def extract(text, regexp):
    result = re.match(string=text, pattern=regexp)
    return result.group()
