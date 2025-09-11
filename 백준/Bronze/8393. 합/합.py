import sys

input = sys.stdin.readline

N = int(input())
M = 0

for i in range(1, N+1):
    M += i

print(M)