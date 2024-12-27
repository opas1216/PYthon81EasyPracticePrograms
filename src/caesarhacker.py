print('Enter the encrypted Caesar cipher message to hack.')
message = input('>')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num -= key
            if num < 0:
                num += len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += symbol

    print(f"Key #{key}: {translated}")