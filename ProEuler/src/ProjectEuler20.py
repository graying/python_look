'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


aNum = 1
for good in range (1,101): # same result if you change 100 to 101,
    aNum = aNum*good

#aNum=103482348723497

aStr = str(aNum)

aSum = 0
for c in aStr:
    Num = int(c)
    aSum += Num
    print("C={0} and Sum = {1}".format(Num, aSum))
    