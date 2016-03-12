#!/usr/bin/python
'''
see http://projecteuler.net/problem=18
'''
# start here

numList = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60 , 4, 23]
]
   
def doCalc(line, cur, value):
    
    if cur[0] == 14:
        global ansList
        ansList.append(list(line))
#        print(line)
#        print("value={0}".format(value))
        return
    
    # try left.down first
    curX = cur[0]
    curY = cur[1]
    # value = value + numList[curX][curY]
    curX += 1
    point = [curX, curY]
    leftline = list(line)
    leftline.append(list(point))
    doCalc(leftline, point, value)
    
    # try right.down then
    curX = cur[0]
    curY = cur[1]
    # value = value + numList[curX][curY]
    curX += 1
    curY += 1
    point = [curX, curY]
    rightline = list(line)
    rightline.append(list(point))
    doCalc(rightline, point, value)
    
    
# def onCalc():
#    curList=[]
#    layer = 15
#    for i in range (0, layer):
#        print (i)
#        if i < 1:
#            alist
#        for j in range

ansList = []
startCur = [0, 0]
line = [[0, 0]]
value = 0
bottom = len(numList)

# get all the list
doCalc(line, startCur, value) 

aMax = 0
# calc the result
for a in ansList:
    aSum = 0
    for cur in a:
        x = cur[0]
        y = cur[1]
        aSum += numList[x][y]
    if aSum > aMax:
        aMax = aSum
    print (a, "Sum ={0}|Max={1}".format(aSum, aMax))

print("MAX={0}".format(aMax))
print(len(ansList))
