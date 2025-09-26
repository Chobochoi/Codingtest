import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        
        new_sum = first + (sec * 2)
        
        heapq.heappush(scoville, new_sum)
        
        count += 1
        
    return count
        
    