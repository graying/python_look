#!/usr/bin/python3

'''
#Sum square difference
#Problem 6

#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.b
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


a=0
b=0

for i in range (1, 101):
    a += i**2
    b += i
    print (str(i))
    
print("a="+str(a))
b=b**2
print("b="+str(b))

print("b-a="+str(b-a))


