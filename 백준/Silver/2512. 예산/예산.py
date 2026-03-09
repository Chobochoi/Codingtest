# 260309
# 프로그래머스 유사 문제
import sys

input = sys.stdin.readline

N = int(input())
M_list = list(map(int, input().split()))
total = int(input())

start = 0
end = max(M_list)

while start <= end:
    mid = (start + end) // 2
    
    all_total = 0
    
    for request in M_list:
        if request > mid:
            all_total += mid
        else:
            all_total += request
            
    if all_total <= total:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)