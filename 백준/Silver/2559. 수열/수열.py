import sys

input = sys.stdin.readline

N, M = map(int, input().split())

K = list(map(int, input().split()))

current_sum = sum(K[0:M])

max_sum = current_sum

for i in range(M, N):
    # 맨 왼쪽 값 빼고, 맨 오른쪽 값 더하기
    current_sum = current_sum - K[i-M] + K[i]
    
    max_sum = max(max_sum, current_sum)
    
print(max_sum)