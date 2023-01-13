#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if (len(args) == 1):
        print(str(1) + " argument:")
        print("1: " + args[-1])
    elif(len(args) <= 0):
        print(str(0) + " arguments.")
    else:
        print(str(len(args)) + " arguments:")
        for i in range(len(args)):
            print(str(i+1)+": " + str(args[i]))
