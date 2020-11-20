#!/usr/bin/python
import sys
from single_byte_xor import xorBruteForce

def detectXor(encrypted):
    return xorBruteForce(encrypted)

def main():
    handle = open("detect_xor_input.txt", "r")
    [print(detectXor(int(line.format(line.strip()), 16))) for line in handle]

if __name__ == "__main__":
    main()
