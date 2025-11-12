def solution(babbling):  
    
    st = ["aya", "ye", "woo", "ma"]
    answer = 0   
    
    for i in babbling:
        result = 0
        for j in range(4):
            if i.find(st[j]) != -1:
                result += len(st[j])
        
        if len(i) == result:
            answer += 1
            
    return answer
            