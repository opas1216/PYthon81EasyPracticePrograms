import sys, time

print('Enter a starting number(greater than 0) or QUIT.')
response = input('> ')
if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = (n * 3) + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)



# Another mode
print('Enter a ending number(greater than 0) or QUIT.')
response = input('> ')
if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()
n = int(response)
for i in range(1, n + 1):
    print(i, end='', flush=True)
    count = 0
    while i != 1:
        count += 1
        if i % 2 == 0:
            i //= 2
        else:
            i = (i * 3) + 1
        print(', ' + str(i), end='', flush=True)
        # time.sleep(0.1)
    print()
    print(f"Result: {count}")

