import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST = []

for i in range(N):
    ST.append(int(input()))
    
ST.sort()

start = 1
end = max(ST) - min(ST)

# 1, 2, 4, 8, 9

result = 0

while start <= end:
    total = 1
    mid = (start + end) // 2
    current = ST[0]
        
    for x in range(1, len(ST)):
        if ST[x] >= current + mid:
            total += 1
            current = ST[x]
            
    if total >= M:
        start = mid + 1
        result = mid
    else:
        end = mid -1
        
print(result)