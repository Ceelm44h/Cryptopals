#!/usr/bin/python
import sys, operator, getopt

charFrequency = " etaoinshrdlucmfwypvbgkjqxz"

def xorBruteForce(text, tries):
    text, chars = hex(text), dict()
    textBytes = [text[i:i+2] for i in range(2, len(text), 2)] #split text to bytes
    
    for byte in textBytes: #count frequency of bytes
        if byte in chars:
            chars[byte] += 1
        else:
            chars[byte] = 1

    mostFrequent = int(max(chars.items(), key = operator.itemgetter(1))[0], 16)
    for keyTry in range(tries):
        key = ord(charFrequency[keyTry]) ^ mostFrequent #xor the most frequent value with letter proposal to get key
        output = [chr(int(text[i:i+2], 16) ^ key) for i in range(2, len(text), 2)]
        
        for char in output:
            print(char, end = "")
        print("")

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"n:ai:",["number=","all", "input="])
    except getopt.GetoptError:
        print("single-byte-xor.py [-n <number of tries> -a] <hex>")
        sys.exit(2)
    text, tries = None, 3

    for opt, arg in opts:
        try:
            if opt in ["-n", "--number"]:
                tries = min(int(arg), len(charFrequency))
            elif opt in ["-a", "--all"]:
                tries = len(charFrequency)
            elif opt in ["-i", "--input"]:
                text = int(arg, 16)
        except ValueError:
            print("single-byte-xor.py [-n <number of tries> -a] <hex>")
            sys.exit(2)

    if text == None:
        print("single-byte-xor.py [-n <number of tries> -a] <hex>")
        sys.exit(2)
    
    xorBruteForce(text, tries)

if __name__ == "__main__":
    main(sys.argv[1:])
    #0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736