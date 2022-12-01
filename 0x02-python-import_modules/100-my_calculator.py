#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    args = argv[1:]
    if argc != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(args[0])
    b = int(args[2])
    op = args[1]
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)