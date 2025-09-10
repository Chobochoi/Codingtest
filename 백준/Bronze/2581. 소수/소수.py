import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
cnt = 0

ST = []

for i in range(M, N+1):
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0 and i != 1:
        ST.append(i)
    cnt = 0

if len(ST) == 0:
    print(-1)
else:
    print(sum(ST))
    print(min(ST))