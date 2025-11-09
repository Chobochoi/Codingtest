import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    A, B = list(map(int, input().split()))

    print(f'Case #{i+1}: {A} + {B} = {A+B}')    
