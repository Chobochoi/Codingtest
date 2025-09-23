def solution(clothes):
    dic = {}
      
    for name, kind in clothes:
        if kind in dic:
            dic[kind] += [name]
        else:
            dic[kind] = [name]
            
    answer = 1
    
    for value in dic:
        answer *= len(dic[value]) + 1
        
    return answer-1
    
    
        
        