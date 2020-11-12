#!/usr/bin/python
import math
import sys

def main(argv):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    for arg in argv:
        try:
            hexNumber = int(arg, 16)
        except ValueError:
            print("hex2base64.py <hex>")
            sys.exit(2)

        encoded = ""
        i = math.ceil(math.log(hexNumber, 2))
        i -= i%4 + 2

        if i % 6 != 0:
            offset = 6 - i%6
            hexNumber = hexNumber << offset
            i += offset
        else:
            offset = 0

        while i >= 0:
            ch = ((hexNumber & (63 << i)) >> i)
            encoded += base64[ch]
            i -= 6

        for i in range(int(offset/2)):
            encoded += "="

        print(encoded)

if __name__ == "__main__":
   main(sys.argv[1:])