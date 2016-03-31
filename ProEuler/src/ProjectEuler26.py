"""
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from decimal import *

print (getcontext())

getcontext().prec = 150


def find_repetent(Num):
    strNum = "%s" % Num
    total_length = len(strNum)
    if total_length == 1:
        print  strNum
        return 0
    elif total_length == 2:
        print  strNum
        return 0
    elif total_length == 3:
        print  strNum
        return 1
    elif total_length == 4:
        print  strNum
        return 2

    pos = strNum.find(".")
    pos = pos + 1
    length = 0
    while True:
        print "pos   =", strNum[pos:pos+length]
        print "pos*2 =", strNum[pos+length+1:]
        print "pos*3 =", strNum[pos * 2:pos * 3 + length]
        if ((strNum[pos:length] == strNum[pos * 2:pos * 2 + length]) and
                (strNum[pos * 2:pos * 2 + length] == strNum[pos * 2:pos * 3 + length])):
            print (strNum[pos:pos + length], length)
            return length
        length += 1
        if length > 59:
            print ("error find, the length of repetent is longer than 49 digits")
            break;
    return 0


for a in range(2, 20):
    Up = 1
    while Up * 10 < a:
        Up = Up * 10
    find_repetent(Up / Decimal(6))
    # print (Up / Decimal(a))
    # print a, Up / Decimal(a)
