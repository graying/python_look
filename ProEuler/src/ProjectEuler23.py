'''
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
'''
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

def testNum(Num):
    if sum(allDivisor(Num)) == Num :
        return "Perfect"
    elif sum(allDivisor(Num)) < Num:
        return "Deficient"
    else: #sum(allDivisor(Num)) > Num:
        return "Abundant"
    
        
for aNum in range (1, 100):
    print (aNum, allDivisor(aNum), testNum(aNum))    
