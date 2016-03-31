'''
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. 
So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''
namefile = open("names.txt", 'rt')
aName = namefile.read()
namefile.close()
nameList = aName.split(',')
nameList.sort()

aTotal = 0
for i in range(0, len(nameList)):
    nameStr = nameList[i]
    aSum = 0
    for c in nameStr:
        if ord(c) in range(ord('A'), ord('Z')+1):
            aSum += (ord(c) - ord('A') + 1)
    aResult = (i + 1) * aSum
    aTotal += aResult
    print (nameStr + ' Pos ={0} sum = {1} result = {2} Total = {3}'.format(i + 1,
                                                                         aSum,
                                                                         aResult,
                                                                         aTotal))
