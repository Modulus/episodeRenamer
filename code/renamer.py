

from os import listdir, replace
import code.regexp_util as rx
import re
from os.path import isfile, join


def rename(name, regexp, split):
    if name and regexp and split:
        eps_nr = rx.extract(name, regexp)

        parts = eps_nr.split(split, 1)

        if len(parts) >= 2:
            parts[0] = "S"+parts[0]
            parts[1] = "E"+parts[1]
        return re.sub(regexp, "".join(str(x) for x in parts), name)
    return None


def rename_files(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print("Before rename!")
    [print(f) for f in files]

    for file in files:
        old_fullname = join(path, file)
        new_file = rename(file,  r"(\d+)(.*)(\d+)", ".")
        new_fullname = join(path, new_file)
        replace(old_fullname, new_fullname)

    files = [f for f in listdir(path) if isfile(join(path, f))]
    print("Afters rename!")
    [print(f) for f in files]

def rename_files(path, regexp, splitter):
    result = rename(text, r"(\d+)(\w*)(\d+)", "e")
