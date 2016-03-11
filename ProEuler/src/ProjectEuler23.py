"""
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper 
divisors is exactly equal to the number. For example, the sum 
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper 
divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant 
numbers is 24. By mathematical analysis, it can be shown that all 
integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced any 
further by analysis even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less 
than this limit.

Find the sum of all the positive integers which cannot be written 
as the sum of two abundant numbers.
Add by Eddy: ths answer is 4179871
"""


def allDivisor(Num):
    if Num == 1:
        return [1]
    elif Num == 2:
        return [1, 2]

    aEnd = (Num // 2)
    divList = [1]
    for Div in range(2, aEnd + 1):
        if Num % Div == 0:
            divList.append(Div)
    return divList


def testnum(Num):
    if sum(allDivisor(Num)) == Num:
        return "Perfect"
    elif sum(allDivisor(Num)) < Num:
        return "Deficient"
    else:  # sum(allDivisor(Num)) > Num:
        return "Abundant"


perfList = []
defiList = []
abunList = []

for aNum in range(12, 28123):
    if testnum(aNum) == "Abundant":
        abunList.append(aNum)
        # print (aNum, allDivisor(aNum), result)

total = len(abunList)
# print (12 in abunList)

numList = []


def isitsumby2abun(Num):
    for A in range(0, total):
        firstnum = abunList[A]
        secondnum = Num - firstnum
        if secondnum == firstnum:
            return True
        elif secondnum <= 0:
            return False
        elif secondnum in abunList:
            return True
    return False


sumnumber = 0
for Number in range(1, 28123):
    isit = isitsumby2abun(Number)
    if (isit):
        print ('don not count this one')
    else:
        sumnumber += Number
    print (Number, "  ", isit, "   Sum=", sumnumber)
