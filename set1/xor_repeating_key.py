#!/usr/bin/python
import sys, operator

def xorWithKey(text, key):
    output = [hex(ord(text[i])^ord(key[i%len(key)]))[2:] for i in range(len(text))]
    return "".join(output)
def main(argv):
    try:
        text, key = argv[0], argv[1]
    except IndexError:
        print("usage: xor_repeating_key.py <plaintext> <key>")
        sys.exit(2)
    
    print(xorWithKey(text, key))

if __name__ == "__main__":
    main(sys.argv[1:])