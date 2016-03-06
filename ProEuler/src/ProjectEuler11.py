#!/usr/bin/python3
'''
Largest product in a grid
Problem 11
In the 20x20 grid below, four numbers along a diagonal line
have been marked in red.
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the
same direction (up, down, left, right, or diagonally) in the 20×20 grid?

'''
#start here
#import math

data = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

adata = data.split('\n') #remove the '\n' at the end of each line and re-organized in a list
matrix = []
for row in adata: #remove the space of between each numbers and split in to matrix
    matrix.append(row.split(' '))

#print(matrix[0][0]) # test the matrix, please be aware the members in matrix is String NOT integer.

aMax = 0
how_many_row = len(matrix)
how_many_col =len(matrix[0])

#for cRow in range(0,how_many_row):
#    for cCol in range (0, how_many_col):
#        print (matrix[cRow][cCol], end=" ")
#    print ("\n")
#

def hasRight(cRow,cCol,):
    if cCol + 3 >= how_many_col:
        return False
    return True

def hasDown(cRow,cCol,):
    if cRow+3 >= how_many_row:
        return False
    return True

def hasRightDown(cRow,cCol,):
    if not hasRight(cRow, cCol):
        return False
    if not hasDown(cRow, cCol):
        return False
    return True

def hasRightUp(cRow,cCol,):
    if not hasRight(cRow, cCol):
        return False
    if cRow < 3:
        return False
    return True


print("how_many_row={0}".format(how_many_row))
print("how_many_col={0}".format(how_many_col))

for cRow in range(0,how_many_row):
    for cCol in range (0, how_many_col):
        if hasRight(cRow, cCol): #product of right 4
            a = int(matrix[cRow][cCol])
            b = int(matrix[cRow][cCol+1])
            c = int(matrix[cRow][cCol+2])
            d = int(matrix[cRow][cCol+3])
            product = a*b*c*d
            if aMax < product:
                aMax = product
                print ("max={2} updated at Row={0} and Col={1} with Right 4".format(cRow, cCol, aMax))

        if hasDown(cRow, cCol): #product of down 4
            a = int(matrix[cRow][cCol])
            b = int(matrix[cRow+1][cCol])
            c = int(matrix[cRow+2][cCol])
            d = int(matrix[cRow+3][cCol])
            product = a*b*c*d
            if aMax < product:
                aMax = product
                print ("max={2} updated at Row={0} and Col={1} with down 4".format(cRow, cCol, aMax))

        if hasRightDown(cRow, cCol): #product of Right down 4
            a = int(matrix[cRow][cCol])
            b = int(matrix[cRow+1][cCol+1])
            c = int(matrix[cRow+2][cCol+2])
            d = int(matrix[cRow+3][cCol+3])
            product = a*b*c*d
            if aMax < product:
                aMax = product
                print ("max={2} updated at Row={0} and Col={1} with RightDown 4".format(cRow, cCol, aMax))

        if hasRightUp(cRow, cCol): #product of Right down 4
            a = int(matrix[cRow][cCol])
            b = int(matrix[cRow-1][cCol+1])
            c = int(matrix[cRow-2][cCol+2])
            d = int(matrix[cRow-3][cCol+3])
            product = a*b*c*d
            if aMax < product:
                aMax = product
                print ("max={2} updated at Row={0} and Col={1} with RightUp 4".format(cRow, cCol, aMax))

#    print ("current max= {0} in {1} rows".format(aMax, cRow))
for cRow in range(0,how_many_row):
    for cCol in range(0, how_many_col):
        print (matrix[cRow][cCol], end=" ")
    print ("\n")
