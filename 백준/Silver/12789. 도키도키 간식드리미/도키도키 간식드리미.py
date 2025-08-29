import sys

input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
ST = []

target = 1

for student in line:
    ST.append(student)
    
    while ST and ST[-1] == target:
        ST.pop()
        target += 1
        
if ST:
    print('Sad')
else:
    print('Nice')   
    
