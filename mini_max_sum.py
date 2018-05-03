#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    sums = []
    # get the sum without the first number
    sums.append(arr[1]+arr[2]+arr[3]+arr[4])
    # get the sum without the second number
    sums.append(arr[0]+arr[2]+arr[3]+arr[4])
    # get the sum without the third number
    sums.append(arr[0]+arr[1]+arr[3]+arr[4])
    # get the sum without the fourth number
    sums.append(arr[0]+arr[1]+arr[2]+arr[4])
    # get the sum without the fifth number
    sums.append(arr[0]+arr[1]+arr[2]+arr[3])
    
    print('{} {}'.format(min(sums), max(sums)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
