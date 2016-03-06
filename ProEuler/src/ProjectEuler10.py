#!/usr/bin/python

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math

def isPrime(num):
    if num==2:
        return True
    if num % 2 ==0:
        return False
      #print(halfnum)
    for i in range(3, int(math.ceil(math.sqrt(num)) + 1), 2):
        #Learned this mothed from http://codereview.stackexchange.com/questions/11317/prime-factorization-of-a-number
        if num % i == 0:
            #print (str(num)+" can be divided by "+str(i)+"="+str(num/i))
            return False
    return True

aSum=2;
for i in range(3, 2000000, 2):
    if isPrime(i):
        aSum+=i

print(aSum)