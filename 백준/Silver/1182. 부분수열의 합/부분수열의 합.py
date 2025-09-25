from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    for c in combinations(K, i):
        if sum(c) == M:
            cnt += 1

print(cnt)