import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ST = []

def backtracking(start):
    if len(ST) == M:
        print(' '.join(map(str, ST)))
        
    for i in range(start, N+1):
        if i not in ST:
            ST.append(i)
            backtracking(i+1)
            ST.pop()

backtracking(1)