
N = int(input())
M = list(map(int, input().split()))


n = int(input())
m = list(map(int, input().split()))

M.sort(reverse=True)

dic = {}

for x in M:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
        
for value in m:
    if value in dic:
        print(dic[value], end =' ')
    else:
        print(0, end = ' ') 