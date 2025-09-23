def solution(clothes):
    
    dic = {}
        
    for name, kind in clothes:
        if kind in dic.keys():
            dic[kind] += [name]
        else:
            dic[kind] = [name]
            
    answer = 1
    for _, y in dic.items():
        answer *= (len(y) + 1)
        
    return answer - 1
    
        
        