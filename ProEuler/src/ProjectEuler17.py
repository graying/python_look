#!/usr/bin/python
'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

'''
# start here
lowWords = ['Zero',
            'One', 'Two', 'Three', 'Four', 'Five',
            'Six', 'Seven', 'Eight', 'Nine', 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']

highWords = {}
highWords[2] = "Twenty"
highWords[3] = "Thirty"
highWords[4] = "Forty"
highWords[5] = "Fifty"
highWords[6] = "Sixty"
highWords[7] = "Seventy"
highWords[8] = "Eighty"
highWords[9] = "Ninety"


def hundred_word(num):
    def tens(num):
        if num >= 100 or num < 0:
            return "error"
        
        if num <= 20:
            return lowWords[num]
        else:
            hNum = num // 10
            lNum = num % 10
            if lNum == 0:
                return highWords[hNum]
            return highWords[hNum] + '-' + lowWords[lNum]
    
    if num >= 1000:
        print("the number should between 0 and 1000")
        return
    elif num == 0:
        return ''
    elif num < 99:
        return tens(num)
    else:
        a = num // 100
        b = num % 100
        Word = lowWords[a] + ' ' + 'Hundred'
        if b == 0:
            return Word
        else:
            return Word + ' and ' + tens(b)


def num2word(num):
    if num > 999999:
        print(" the number is too big, it should be within 1 million")
        return
    numK = num // 1000
    numH = num % 1000
    if num < 1000:
        KWord = ''
    else:
        KWord = hundred_word(numK) + ' ' + 'Thousand'
    
    if numH == 0:
        return KWord
    else:
        HWord = hundred_word(numH)
    
    if KWord == '':
        return HWord
    
    return KWord + ' ' + HWord

length = 0
for i in range(1, 1001):
    myStr = num2word(i)
    print (myStr, end='|')
    a = myStr.replace(' ', '')
    b = a.replace('-', '')
    length += len(b)
    print (b, len(b), length)