import sys

input = sys.stdin.readline

N = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x,y = map(int, input().split())
    
    for xValue in range (x, x+10):
        for yValue in range (y, y+10):
            if xValue >= 100 or yValue >= 100:
                break
            paper[xValue][yValue] = 1

sum = 0

for row in range(100):
    sum += paper[row].count(1)
    
print(sum)