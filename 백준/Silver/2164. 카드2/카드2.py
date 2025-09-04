import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) > 1):
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)
    
print(deque[0])