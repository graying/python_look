#!/usr/bin/python
'''

this program doesn't work out the result, anyway, I use this program try
20x1 grid = 21 pathes
20x2 grid = 231pathes
20x3 grid = 1771 pathes
20x4 grid = 10626 pathes
finally I found the patten that according to the row inclusing, the result should be
>>> a1 = 21
>>> a2 = 20*a1/2+a1
>>> a3 = 20*a2/3+a2
>>> a4 = 20*a3/4+a3
... ...
>>> a15 = 20*a14/15+a14
>>> a16 = 20*a15/16+a15
>>> a17 = 20*a16/17+a16
>>> a18 = 20*a17/18+a17
>>> a19 = 20*a18/19+a18
>>> a20 = 20*a19/20+a19

137846528820

see gridpath.py for a better usage of this program 
'''

#start here
startPoint = [0, 0]
endPoint = [20, 20]

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
  
