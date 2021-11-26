# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
def detemineSudoku(array,i,j,number):
    for j1 in range(0,9):
        if(array[i,j1]==number and j1!=j):
            return False
    for i1 in range(0,9):
        if(array[i1,j]==number and i1!=i):
            return False
    x1=i//3
    y1=j//3
    for i2 in range(3*x1,3*x1+3):
        for j2 in range(3*y1,3*y1+3):
            if(array[i2,j2]==number and (i2!=i or j2!=j)):
                return False
    return True
def Sudoku(array,n,List):
    if(n>80):
        print(arr)
        return;
    else:
        i=n//9
        j=n%9
        if(array[i,j]!='.'):
            Sudoku(array,n+1,List)
        else:
            for number in range(1,10):
                if(detemineSudoku(array,i,j,str(number))):
                    arr[i,j]=str(number)
                    Sudoku(array,n+1,List)
                    arr[i,j]='.'
arr=np.array([['5','3','.','.','7','.','.','.','.'],
              ['6','.','.','1','9','5','.','.','.'],
              ['.','9','8','.','.','.','.','6','.'],
              ['8','.','.','.','6','.','.','.','3'],
              ['4','.','.','8','.','3','.','.','1'],
              ['7','.','.','.','2','.','.','.','6'],
              ['.','6','.','.','.','.','2','8','.'],
              ['.','.','.','4','1','9','.','.','5'],
              ['.','.','.','.','8','.','.','7','9'],])
print(arr)
List=[]
Sudoku(arr,0,List)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
