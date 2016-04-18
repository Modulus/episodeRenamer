#!/usr/bin/python
from code import renamer
import sys

if __name__ == "__main__":
    print("Program called with {}", sys.argv)

    if sys.argv and len(sys.argv) > 0 and sys.argv[1] is "--help":
        print("Program should be called with a directory as the only argument")
        print("main.py \"H:\shows\"")
        print("You may also use regular expressions, like so:")

    elif sys.argv and len(sys.argv) < 0:
        raise FileNotFoundError("You need to enter the name of a directory for this to work")

    elif sys.argv and len(sys.argv) == 2:
        path = sys.argv[1]
        renamer.rename_files(path)
    elif sys.argv and len(sys.argv) > 2:
        path = sys.argv[1]
        split = sys.argv[2]
        renamer.rename(path, r"(\d+)(.*)(\d+)", split)
    else:
        print("You managed to screw this up some how..., write main py --help for actual help, we will send someone")
