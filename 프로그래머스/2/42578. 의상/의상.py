#260323
def solution(clothes):
    
    dic = {}
        
    for name, kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
            
    answer = 1
    
    for num in dic.values():
        answer *= (num + 1)
        
    return answer - 1
    
    
            
    
        