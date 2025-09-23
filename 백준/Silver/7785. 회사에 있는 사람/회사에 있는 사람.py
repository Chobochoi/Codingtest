N = int(input())

dic = {}

for _ in range(N):
    name, inout = map(str, input().split())
    if inout == 'enter':
        dic[name] = inout
    else:
        del dic[name]

dic = sorted(dic, reverse = True)

for i in dic:
    print(i)