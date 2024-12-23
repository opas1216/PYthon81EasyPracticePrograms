"""Bitmap Message, by Al Swrigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic"""

import sys


# (!) Try changing this multiline string to any image you like:
#
# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
#  https://inventwithpython.com/bitmapworld.txt)

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""
print('Bitmap Message, by Al Swrigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for index, bit in enumerate(line):
        if bit == ' ':
            print(' ',end='')
        else:
            print(message[index % len(message)], end='')
    print()
