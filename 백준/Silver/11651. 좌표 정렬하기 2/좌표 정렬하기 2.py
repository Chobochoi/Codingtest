import sys

input = sys.stdin.readline

N = int(input())
ST= []

for _ in range(N):
    x, y = map(int, input().split())
    ST.append([y, x])    
    
ST.sort()

for i in range(N):
    print(ST[i][1], ST[i][0])