import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ST = []

for i in range(1, N+1):  
    if N % i == 0:
        ST.append(i)
        

if len(ST) < M:
    print(0)
else:
    print(ST[M-1])