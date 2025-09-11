import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST= []

# 비내림차순으로
def dfs(start):
    if(len(ST)) == M:
        print(' '.join(map(str, ST)))
        return
    
    for i in range(start, N+1):
        ST.append(i)
        dfs(i)
        ST.pop()

dfs(1)