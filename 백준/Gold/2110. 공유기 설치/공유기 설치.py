# 260310
# 프로그래머스 유사 문제
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
st = []

for i in range(N):
    st.append(int(input()))
        
st.sort()
    
start = 1
end = st[-1] - st[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = st[0]
    
    for i in range(1, len(st)):
        if st[i] >= current + mid:
            count += 1
            current = st[i]
            
    if count >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)