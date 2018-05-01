import os
import sys

def diagonalDifference(a):
    alist = []
    blist = []
    lis = len(a[0])
    # create the list for first diagonal
    for i in range(lis):
        alist.append(a[i][i])
    # create the list for second diagonal
    for j in range(lis-1,-1,-1):
        blist.append(a[lis-1-j][j])
    
    # get the sum of first array
    suma = sum(alist)
    # get the sum of second array
    sumb = sum(blist)
    # get the difference of the diagonal
    sumt = suma - sumb
    
    return abs(sumt)
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()