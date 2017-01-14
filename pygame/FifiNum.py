"""guess the number game for Fifi"""

import random
import sys

if len(sys.argv) < 2:
    maxnumber = 25
else:
    maxnumber = int(sys.argv[1])


def GenerateNumber():
    # type: () -> object
    random.seed()
    return random.randrange(1, maxnumber)


number = GenerateNumber()
myGuess = -1
tried = 0
aprompt = "input your number between 1-"+str(maxnumber)+":"
# print number, myGuess

while True:
    myGuess = int(raw_input(aprompt))
    tried += 1
    if myGuess > number:
        print "your number is too large! try again"
    if myGuess < number:
        print "Your number is too small! try again"
    if myGuess == number:
        print "Yes! You guessed right!!! in", tried, "times"
        break
