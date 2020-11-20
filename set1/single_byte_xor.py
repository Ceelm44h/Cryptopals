#!/usr/bin/python
import sys, operator

frequency = { 'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }

def xorBruteForce(text):
    text, bestScore = hex(text), -1
    for keyTry in range(256):
        score = 0
        output = [chr(int(text[i:i+2], 16) ^ keyTry) for i in range(2, len(text), 2)] #decode
        for ch in output:
            if ch in frequency:
                score += frequency[ch.lower()]
        if score > bestScore:
            bestScore = score
            bestOutput = "".join(output)

    return "".join(bestOutput)

def main(argv):
    text = None
    if len(argv) == 0:
        print("single-byte-xor.py <hex>")
        sys.exit(2)
    try:
        text = int(argv[0], 16)
    except ValueError:
        print("single-byte-xor.py <hex>")
        sys.exit(2)
    
    print(xorBruteForce(text))

if __name__ == "__main__":
    main(sys.argv[1:])
    #0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736