import os
import sys

def plusMinus(arr):
    arlen = len(arr)
    pos = []
    neg = []
    zer = []
    for item in arr:
        if item > 0:
            pos.append(item)
        if item < 0:
            neg.append(item)
        if item == 0:
            zer.append(item)
    print(len(pos) / arlen)
    print(len(neg) / arlen)
    print(len(zer) / arlen)
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)