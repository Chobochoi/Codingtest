import sys
input = sys.stdin.readline

cnt = 0
ST = []
    
for value in range(1, 11):
    M = int(input())
    N = M % 42
    ST.append(N)
    ST.sort()

list_ST = list(set(ST))

print(len(list_ST)) 