"""Caesar Cipher, by Al Sweigart@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostatch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math
"""

try:
    import pyperclip
except ImportError:
    pass

# Symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over a key number. For example, a key of 2 means the letter '
      'A is encrypted into C, the letter B encrypted into D, and so on.')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key(0 to {maxKey}) to use.')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print(f'Enter the message to {mode}.')
message = input('> ')

# Caesar cipher only works on uppercase letters
message = message.upper()

translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        translated += SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard.')
except:
    pass