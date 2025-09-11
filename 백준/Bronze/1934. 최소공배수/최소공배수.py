import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    A, B  = map(int, input().split())
    if A < B:
        Min = A
        Max = B
    else :
        Min = B
        Max = A
    while Max % Min != 0:
        temp = Max % Min
        Max = Min
        Min = temp  #최대공약수
    answer =  Min * (A//Min) * (B//Min)
    print(answer)