import datetime, random
from http.cookiejar import MONTHS


def getBrithdays(numberOfBirthdays: int):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays: list):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1: ]):
            if birthdayA == birthdayB:
                return birthdayA

print('''Birthday Paradox, by AL Sweigart al@inventwithpython.com
The Birthdat Paradox shows us that in a group of N people, the odds
 that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
 simulations) to explore this concept.
 
 (It's not actually a paradox, it's just a surprising result.
 ''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'OCT', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (MAX 100')
    response = input('> ')
    if response.isdecimal() and(0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print('Here are', numBDays, 'birthdays:')
birthdays = getBrithdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month-1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another100,000 simulations')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBrithdays(numBDays)
    if getMatch((birthdays)) != None:
        simMatch += 1
print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a\n' \
      'matching brithday in that group', simMatch, 'times. This means\n' \
      'that', numBDays, 'people have a', probability, '% chance of\n' \
      'having a matching birthday in their group.\n' \
      'That\'s probably more than you would think!')


