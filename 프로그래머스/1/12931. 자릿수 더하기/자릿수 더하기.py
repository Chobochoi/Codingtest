def solution(n):
    answer = 0
    
    ST = list(str(n))
    
    for i in ST:
        answer += int(i)
        
    return answer