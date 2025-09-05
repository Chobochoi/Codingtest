import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deque = deque()

for _ in range(N):
    M = list(map(int, input().split())) 
    
    if M[0]==1:
        deque.appendleft(M[1])
    elif M[0]==2:
        deque.append(M[1])
    elif M[0]==3:
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif M[0]==4:
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif M[0] == 5:
        print(len(deque))
    elif M[0] == 6:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif M[0] == 7:
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif M[0] == 8:
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)         
        
        
        

   
   
