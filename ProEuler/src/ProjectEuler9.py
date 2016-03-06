#!/usr/bin/python

'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def isPythTri(a,b,c):
    return ((a**2)+(b**2) == (c**2))

find=False
for a in range(1,500):
    for b in range(a+1,500):
        c = 1000-(a+b)
        if isPythTri(a, b, c):
            print("hello")
            print("{0}-{1}-{2}".format(a,b,c))
            print("a*b*c={0}".format(a*b*c))
            find=True
            break
    if (find):
        break