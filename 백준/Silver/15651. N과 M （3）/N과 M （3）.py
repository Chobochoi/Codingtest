import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST = []

def backtracking():
    if len(ST) == M:
        print(' '.join(map(str, ST)))
        return              
           
    for i in range(1, N+1):
        ST.append(i)
        backtracking()
        ST.pop()
            
backtracking()