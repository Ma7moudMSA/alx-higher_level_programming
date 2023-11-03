#!/usr/bin/python3
from sys import argv
i = 1
length = len(argv)
sum = 0
if __name__ == '__main__':
    for num in range(1, length):
        sum += int(argv[num])
print(sum)
