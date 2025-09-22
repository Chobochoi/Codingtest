def solution(clothes):
    dic_clothes ={}
    
    for name, kind in clothes:
        if kind in dic_clothes.keys():
            dic_clothes[kind] += [name]
        else:
            dic_clothes[kind] = [name]
            
    answer = 1
    for _, value in dic_clothes.items():
        answer *= (len(value) + 1)
        
    return answer -1
    
