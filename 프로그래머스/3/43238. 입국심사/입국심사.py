def solution(n, times):
    answer = 0    
    start = 1
    end = n * max(times)
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            end = mid - 1
        elif people < n:
            start = mid + 1
    return answer
            