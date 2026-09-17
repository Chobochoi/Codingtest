from collections import Counter

def solution(clothes): 
    answer = 1
    
    types = [item[1] for item in clothes]
    
    counter = Counter(types)
     
    for count in counter.values():
        answer *= (count + 1)        
    
    return answer - 1  
            
    
        