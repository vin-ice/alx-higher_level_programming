#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    args = argv[1:]
    print("{} {}{}".format(argc, "argument" if argc == 1 else "arguments", ":"  if argc > 0 else "."))
    for index, arg in enumerate(args, start=1):
        print("{}: {}".format(index, arg))