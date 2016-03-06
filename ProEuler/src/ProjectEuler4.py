#!/usr/bin/python3

'''
#Largest palindrome product
#Problem 4
#a palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindromic(num):
    alist=[]
    if num < 10:
        alist.insert(0, num)
        return False
    while num > 10:
        alist.insert(0, (num % 10))
        num = num // 10
    alist.insert(0, num)
    
    lenth = len(alist)
    if lenth <= 1:
        return False
    halfLenth=lenth//2
    
    cursor = 0
    while lenth > halfLenth:
        if alist[cursor] != alist[lenth-1]:
            return False
        cursor +=1
        lenth -=1
    return True;
        
#print(isPalindromic(9876789))
result=[]
a=999
while a>=1:
    
    b=999
    while b>=1:
        if isPalindromic(a*b):
            print ("a="+str(a))
            print ("b="+str(b))
            print ("a*b="+str(a*b))
            result.append(a*b)
        b-=1
    a-=1

print(max(result))
