import sys
input = sys.stdin.readline

Total = int(input())

X = int(input())

sumab = 0

for i in range(X):
    a, b = map(int, input().split())

    sumab += a * b


if sumab == Total:
    print('Yes')
else:
    print('No')