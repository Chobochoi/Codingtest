import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST= [0] * N

for row in range(M):
    i,j,k = map(int, input().split())
    for col in range(i, j+1):
        ST[col - 1] = k
        
for col in range(N):
    print(ST[col], end=" ")
