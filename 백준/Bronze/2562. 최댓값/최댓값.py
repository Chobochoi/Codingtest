import sys
input = sys.stdin.readline

ST= []

for _ in range(9):
    N = int(input())
    ST.append(N)
        
print(max(ST))
print(ST.index(max(ST))+1)
