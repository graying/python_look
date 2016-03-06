#!/usr/bin/python3

'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def div_by_all(num):
    for i in range(20, 1, -1):
        if num % i !=0:
            return False
    return True;
        
a=20*19

while div_by_all(a)==False:
    a+=20
    
print (str(a))
