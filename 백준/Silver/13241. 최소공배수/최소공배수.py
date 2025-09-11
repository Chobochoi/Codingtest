import sys
input = sys.stdin.readline

A, B = map(int, input().split())
answer = 0

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