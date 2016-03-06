#!/usr/bin/python
'''


'''
import sys
#from tkinter import *


if (len(sys.argv)) != 3:
    print("Usage: GridPath.py Rows Columns, samples: python3 GridPath.py 10 20")
    exit(0)
#start here
startPoint = [0, 0]
endPoint = [int(sys.argv[1]), int(sys.argv[2])]
print ("the grid is {0}x{1}".format(endPoint[0],endPoint[1]))

def goNext(apath, aPoint):

    if (aPoint[0] == endPoint[0]) and (aPoint[1]==endPoint[1]): #at the right edge
        global mycount
        mycount += 1
        print ("{0}|".format(mycount), apath)
        return

    if (aPoint[0] < endPoint[0]): #not at the right edge
        newPoint = list(aPoint)
        goright_path = list(apath)
        newPoint[0] = newPoint[0]+1 # go right first
        goright_path.append(newPoint)
        goNext(goright_path, newPoint)
        
    if (aPoint[1] < endPoint[1]): #not at the bottom edge
        newPoint = list(aPoint)
        godown_path = list(apath)
        newPoint[1] = newPoint[1]+1 # go down 1 step
        godown_path.append(newPoint)
        goNext(godown_path, newPoint)
    
path1 = []
mypoint = [0,0]
mycount = 0
path1.append(list(mypoint))
goNext(path1, mypoint)