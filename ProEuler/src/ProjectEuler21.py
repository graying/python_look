'''
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
def allDivisor(Num):
    aList = []
    Top = Num // 2 + 1
    for i in range(1, Top):
        if (Num % i) == 0:
            aList.append(i)
    return aList
aSum = 0
for a in range(1, 10000):
    b = sum(allDivisor(a))  # b=d(a)
    c = sum(allDivisor(b))  # c=d(b)
    if a == c and (a != b):
        aSum += a
        print (a, b, aSum)
        
