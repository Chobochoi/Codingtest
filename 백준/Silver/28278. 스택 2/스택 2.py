import sys

input = sys.stdin.readline
N = int(input())

ST = []

for _ in range(N):
    
    str = sys.stdin.readline().split()
    
    if str[0] == '1':
        ST.append(str[1])
    elif str[0] == '2':
        if ST:
            print(ST.pop())
        else:
            print(-1)
    elif str[0] == '3':
        print(len(ST))
    elif str[0] == '4':
        if ST:
            print(0)
        else:
            print(1)
    elif str[0] == '5':
        if ST:
            print(ST[-1])
        else:
            print(-1)       
