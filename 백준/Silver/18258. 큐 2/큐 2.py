import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deque = deque()

for _ in range(N):
    M = list(map(str, input().split())) 
    
    if M[0]=='push':
        deque.append(M[1])
    elif M[0]=='pop':
        if len(deque) != 0:
            print(deque[0])
            deque.popleft()
        else:
            print(-1)
    elif M[0]=='size': 
        print(len(deque))
    elif M[0]=='empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif M[0]=='front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1) 
    elif M[0]=='back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
