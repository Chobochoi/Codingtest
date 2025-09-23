N = int(input())

for _ in range(N):
    M = int(input())

    dic = {}

    for _ in range(M):
        name, kind = map(str, input().split())
        
        if kind in dic:
            dic[kind] += [name]
        else:
            dic[kind] = [name]  
    
    answer = 1

    for value in dic:      
        answer *= len(dic[value]) + 1

    print(answer-1)       
