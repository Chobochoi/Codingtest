# 260310
# 프로그래머스 유사 문제
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

K = list(map(int, input().split()))

start = 0
end = max(K)
    
while start <= end:
    mid = (start + end) // 2    

    all_total = 0
    
    for tree in K:
        if tree > mid:
            all_total += tree - mid

    if all_total >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)