#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print("0")
    else:
        total = 0
        for i in range(len(sys.argv) - 1):
            total += int(sys.argv[i + 1])
        print("{}".format(total))
