#!/usr/bin/python3

'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

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

count=1
mynum=3
print ("count = {0} | mynum={1}".format(1,2))
while count<10001:
    if isPrime(mynum):
        count +=1
        print ("count = {0} | mynum={1}".format(count,mynum))
    mynum+=2