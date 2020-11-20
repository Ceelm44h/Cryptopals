#!/usr/bin/python
import sys

def main(argv):
    try:
        text = int(argv[0], 16)
        key = int(argv[1], 16)
    except ValueError:
        print("xor.py <hex> <hex>")
        sys.exit(2)

    print(hex(text ^ key))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1:])
    else:
        print("xor.py <hex> <hex>")