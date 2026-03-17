# 260317
# Greedy 알고리즘
# 프로그래머스 유사 문제
import sys

input = sys.stdin.readline

N = int(input())
  
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append([start, end])
    
meetings.sort(key=lambda x : (x[1], x[0]))

count = 0
last_end_time = 0

for m in meetings:
    start = m[0]
    end = m[1]
    
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)