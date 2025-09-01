import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 파이썬에서의 중복 제거 방법은?
# set 함수를 통해서 중복 제거하여 다시 배열에 담기
arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = ' ')