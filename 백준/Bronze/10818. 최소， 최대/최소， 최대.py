import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))

for i in range(N):
    M[i] = int(M[i])
        
print(min(M), max(M))      