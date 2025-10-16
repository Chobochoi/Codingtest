import sys

input = sys.stdin.readline

st = []

N = int(input())

for i in range(N):
    M = input().split()
    
    if M[0] == 'push':
        st.append(M[1])
    elif M[0] == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
            st.pop()
    elif M[0] == 'size':
        print(len(st))
    elif M[0] == 'empty':
        if len(st) == 0:
            print(1)
        else: 
            print(0)
    elif M[0] == 'top':
        if len(st) == 0:
            print(-1)
        else: 
            print(st[-1])       
        
