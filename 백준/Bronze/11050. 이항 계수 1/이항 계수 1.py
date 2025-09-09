import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ST = []
child_sum = 1
sum = 1

# 분자
for i in range(1, N+1):
    ST.append(i)
    
ST.reverse()

for i in range(M):
    child_sum *= ST[i]
    
# 분모
for i in range(1,M+1):
    sum = sum * i    

print(int(child_sum / sum))