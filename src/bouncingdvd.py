"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD lolo animation. You have to be "of a certain age" to appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, bext"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you\n' \
          'can install by following the instructions at\n' \
          'https://pypi.org/project/Bext/')
    sys.exit()

WIDTH, HEIGHT = bext.size()

WIDTH = -1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):





if __name__ == '__main__':
    main()


