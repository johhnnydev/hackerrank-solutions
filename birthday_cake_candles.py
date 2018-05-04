import os
import sys

def birthdayCakeCandles(n, ar):
    tallest = max(ar)
    tallest_candles = []
    for i in ar:
        if i == tallest:
            tallest_candles.append(i)
    return len(tallest_candles)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(n, ar)
    f.write(str(result) + '\n')
    f.close()