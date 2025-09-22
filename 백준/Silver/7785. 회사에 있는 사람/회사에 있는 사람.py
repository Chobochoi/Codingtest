N = int(input())

st = {}

for _ in range(N):
    name, inout = map(str, input().split())
    
    if inout == 'enter':
        st[name] = inout 
    else:
        del st[name]    

st = sorted(st, reverse=True)

for i in st:
    print(i)