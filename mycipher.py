import sys

shift = int(sys.argv[1]) % 26
text = sys.stdin.read()

encoded = ""

for char in text.upper():
    if 'A' <= char <= 'Z':
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        encoded += new_char

blocks = []

for i in range(0, len(encoded), 5):
    blocks.append(encoded[i:i+5])

for i in range(0, len(blocks), 10):
    print(" ".join(blocks[i:i+10]))
