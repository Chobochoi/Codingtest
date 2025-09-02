import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
M = max(num)

for value in range(N):
    num[value] = num[value]/M * 100
    
print(sum(num)/N)