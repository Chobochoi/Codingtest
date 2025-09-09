import sys
input = sys.stdin.readline

N = int(input())
ST = list(map(int, input().split()))
num = []
cnt = 0

for x in ST:
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                cnt += 1
            break
        
print(cnt)