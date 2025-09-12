import sys
input = sys.stdin.readline

def factorial(number):
    num = 1
    for i in range(1, number+1):
        num *= i
    return num

T = int(input())
result = 1

for _ in range(T):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial(N) * factorial(M-N))
    print(result)