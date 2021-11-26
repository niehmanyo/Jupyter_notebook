# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import timeit as tt
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
def Sudoku(array,n):
    if(n>80): ## If n > 80 means all elements are matched,could print this array
        print(arr)
        return;
    else:
        i=n//9
        j=n%9
        if(array[i,j]!='.'):
            Sudoku(array,n+1) ## If meet fix element, we jump this step
        else:
            for number in range(1,10): ##From 1 to 9 to match
                if(detemineSudoku(array,i,j,str(number))): ## if there is no repeated elements
                    arr[i,j]=str(number) # we set this element to be this value
                    Sudoku(array,n+1) ## Then based on this element to do next n+1 elements
                    arr[i,j]='.' ## Import part, if do this steps, means last part Sudoku() fail,so we have to set this element to be '.',
                    # then when backtracking,the elements we set before could change,otherwise,it will exit
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
print("-"*50)
Sudoku(arr,0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
