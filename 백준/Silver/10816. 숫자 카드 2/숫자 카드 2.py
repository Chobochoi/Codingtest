import sys
import collections

input = sys.stdin.readline

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))

N_counter = collections.Counter(Nlist)

answer = []

for m in Mlist:
    # m(카드 번호)가 아닌, N_counter[m](카드의 개수)를 리스트에 넣습니다.
    answer.append(N_counter[m])
    
print(*answer)