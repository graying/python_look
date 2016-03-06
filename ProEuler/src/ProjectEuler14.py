#!/usr/bin/python
'''
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

#start here
def isEven (num):
    return (num % 2) == 0

def findCol(num):
    collist = []
    while num >1:
        if isEven(num):
            collist.append(num/2)
            num = num /2
        else:
            collist.append(num*3+1)
            num = num*3+1
    if num != 1:
        print ("error, the last number is not 1")
    return collist        
    
startNum = 999999
theList = []

while startNum > 1:
    print ("trying {0}".format(startNum))
    colList = findCol(startNum)
    if len(colList) > len(theList):
        theList = colList
        theResult = startNum
        #print("current result is {0} of {1} numbers ".format(startNum, len(theList)), theList)
    startNum -= 2

print ("finished ... the result is {0} of {1} numbers ".format(theResult, len(theList)))
print (theList)