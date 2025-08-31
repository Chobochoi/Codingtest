import sys

input = sys.stdin.readline

N = int(input())
ST= []

for _ in range(N):
    ST.append(list(map(int, input().split())))
    
ST.sort()

for i in range(N):
    print(ST[i][0], ST[i][1])
