import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
deque = deque([i for i in range(1, N+1)])
ST=[] * N

while deque:
    for i in range(M-1):
        deque.append(deque.popleft())
    ST.append(deque.popleft())    



print("<", end = '')
for i in range(len(ST)-1):
    print("%d, " %ST[i], end = '')
print(ST[-1], end ='')
print(">")