N = int(input())

for i in range(N):
    M = int(input())
    
    dic = {}
    
    for i in range(M):
        name, kind = map(str, input().split())
        
        if kind in dic:
            dic[kind] += [name]
        else:
            dic[kind] = [name]
            
    answer = 1
    for value in dic:
        answer *= (len(dic[value])+ 1)
        
    print(answer-1)