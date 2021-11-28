# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
  #  print_hi('PyCharm')
import numpy as np
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def determineOK(arr,i,j):
    for x in range(8):
        if(arr[x,j]==1 and x!=i):#判断第j列不能出现重复的皇后
            return False
    for y in range(8):
        if(arr[i,y]==1 and y!=j):
            return False #判断第i行不能出现重复的皇后
    x1=i-1
    y1=j-1 #(x1,y1)是(i,j)的左上角的顶点
    x2=i-1
    y2=j+1 #(x2,y2)是(i,j)的右上角的顶点
    x3=i+1
    y3=j-1 #(x3,y3)是(i,j)的左下角的顶点
    x4=i+1
    y4=j+1 #(x2,y2)是(i,j)的右下角的顶点
    while(x1>=0 and y1>=0):
        if(arr[x1,y1]==1):
            return False #判断左上斜线是否有皇后
        x1-=1
        y1-=1
    while(x2>=0 and y2<8):
        if(arr[x2,y2]==1):
            return False #判断右上斜线是否有皇后
        x2-=1
        y2+=1
    while(x3<8 and y3>=0):
        if(arr[x3,y3]==1):
            return False #判断左下斜线是否有皇后
        x3+=1
        y3-=1
    while(x4<8 and y4<8):
        if(arr[x4,y4]==1):
            return False #判断右下斜线是否有皇后
        x4+=1
        y4+=1
    return True #以上条件均不满足，就是说明可以防止皇后

def eight_queen(array,n,List):# n是第n行，
    if(n>7):# 因为8*8 矩阵是0-7,所以当n=8>7的时候，就说明已经完成了。
        List.append(array)
        print("This is",List.__len__(),"answer:")
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                print(array[i,j],end="")
            print()
        print("-"*60)
    else:
        for y in range(8): #从第n行开始遍历，然后每一列判断能否防止皇后这样的递推，不行就一直判断每一列，直到不行就递归回去
            if(determineOK(array,n,y)):
                array[n,y]=1
                eight_queen(array,n+1,List)
                array[n,y]=0 #如果八皇后递推里for所有选项不行，说明 n，y这一项有问题，重新变为0
array=np.zeros((8,8),dtype=int)
print(array)
List=[]
eight_queen(array,0,List)