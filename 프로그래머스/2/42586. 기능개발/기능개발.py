def solution(progresses, speeds):
    total_sum = []
    time = 0
    cnt = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else:
            if cnt > 0:
                total_sum.append(cnt)
                cnt = 0
            time += 1
    
    total_sum.append(cnt)
    
    return total_sum
                    
                    
        
            
    

            
            
        
    