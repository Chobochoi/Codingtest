import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST = [0] * N
temp = 0

for change in range(N):
    ST[change] = change + 1
    
for change in range(M):
    i, j = map(int, input().split())
    temp = ST[i-1]
    ST[i-1] = ST[j-1]
    ST[j-1] = temp

for change in range(N):
    print(ST[change], end = " ")   