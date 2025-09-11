import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())
deno = 0
num = 0

if B < D:
    Min = B
    Max = D
else:
    Min = D
    Max = B
while Max % Min != 0:
    temp = Max % Min
    Max = Min
    Min = temp

deno = Min * (B//Min) * (D//Min) #분모
num = A * (D//Min) + C * (B//Min) #분자

newNum = num
newDeno = deno

#한번 더 최대공약수 구해서 나누기 (기약분수)
while newDeno % newNum != 0: 
    result = newDeno % newNum
    newDeno = newNum
    newNum = result
    
print(int(num/newNum), int(deno/newNum))