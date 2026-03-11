# 260311
# 프로그래머스 유사 문제
import sys

input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    word = input().rstrip()
    st = []
    
    for char in word:
        if len(st) != 0 and char == st[-1]:
            st.pop()
        else:
            st.append(char)
            
    if len(st) == 0:
        count += 1
    
print(count)