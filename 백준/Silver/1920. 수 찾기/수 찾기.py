import sys
input = sys.stdin.readline

N = int(input())
listN = list(map(int, input().split()))

M = int(input())
listM = list(map(int, input().split()))

set_listN = set(listN)

for value in listM:
    if value in set_listN:
        print(1)
    else:
        print(0)
