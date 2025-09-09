import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST = list(map(int, input().split()))
pre = [0]
sum = 0

for i in range(N):
    sum += ST[i]
    pre.append(sum)
    
for value in range(M):
    i, j = map(int, input().split())
    print(pre[j] - pre[i-1])
