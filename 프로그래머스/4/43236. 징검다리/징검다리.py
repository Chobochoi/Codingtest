def solution(distance, rocks, n):
    
    rocks.sort()
    rocks.append(distance)
    
    start = 1
    end = distance
    
    answer = 0
    
    while start <= end:
        mid = (start + end)//2
        current = 0
        total = 0
        
        for i in range(len(rocks)):
            prev_current = rocks[i]
            
            if prev_current - current < mid:
                total += 1
                
            else:
                current = prev_current
            
            if n < total:
                break
        
        if total <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid -1
            
    return answer 
    
    