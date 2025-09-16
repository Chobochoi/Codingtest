def solution(n):
    # 출발
    result = 0
       
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            continue
        elif n % 2 == 1:
            n = n - 1
            result = result + 1
            continue
            
    return result
    
    
            
        
        