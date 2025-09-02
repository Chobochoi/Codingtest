import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST= [] * N
temp = 0

for value in range(N):
    ST.append(value + 1)

for value in range(M):
    i, j = list(map(int, input().split()))
    temp = ST[i-1:j]
    temp.reverse()
    ST[i-1:j] = temp
        
for value in range(N):
    print(ST[value], end = " ")