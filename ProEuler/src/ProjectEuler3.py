#!/usr/bin/python3
'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math


def isPrime(num):
    '''
    return True if the given number is Prime, otherwise return False

    '''
    if num == 2:
        return True
    if num % 2 == 0:
        return False
        # print(halfnum)
    for i in range(3, int(math.ceil(math.sqrt(num)) + 1), 2):
        # Learned this mothed from http://codereview.stackexchange.com/questions/11317/prime-factorization-of-a-number
        if num % i == 0:
            # print (str(num)+" can be divided by "+str(i)+"="+str(num/i))
            return False
    return True


if __name__ == "__main__":
    S = 600851475143
    N = int(math.ceil(math.sqrt(S)) + 1)

    while N > 2:
        print ("trying " + str(N))
        if (S % N == 0):
            if isPrime(N):
                print (N)
                break
        N = N - 1
