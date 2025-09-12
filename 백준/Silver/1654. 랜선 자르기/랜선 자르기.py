import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = [int(input()) for i in range(N)]

start = 1
end = max(K)
result = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    
    for i in K:
        cnt += (i // mid)
        
    if cnt >= M:
        result = mid
        start = mid + 1
        
    else:
        end = mid - 1
        
print(result)