#260312
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    total_sum = []
    time = 0
    count = 0
    
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
            
        else:
            if count > 0:
                total_sum.append(count)
                count = 0
            time += 1
            
    total_sum.append(count)
    
    return total_sum
            