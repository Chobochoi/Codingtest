import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

    
for i in range(N):
    Nlist = list(map(int, input().split()))
    print(sum(Nlist))