import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ST = []

def backtracking():
    if len(ST) == M:
        print(' '.join(map(str, ST)))
        
    for i in range(1, N+1):
        if i not in ST:
            ST.append(i)
            backtracking()
            ST.pop()

backtracking()

