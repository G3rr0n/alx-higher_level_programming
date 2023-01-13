#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0
    args = sys.argv[1:]
    for i in range(len(args)):
        result = result + int(args[i])
    print(result)
