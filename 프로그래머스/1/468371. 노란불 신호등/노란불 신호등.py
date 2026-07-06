#260706
#최소공배수를 활용한
import math

def get_lcm_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = (lcm * numbers[i]) // math.gcd(lcm, numbers[i])
    return lcm
    
def solution(signals):
    n = len(signals)
    cycles = []
    
    for g, y, r in signals:
        cycles.append(g + y + r)
        
    max_time = get_lcm_list(cycles)
    
    for t in range(max_time):
        all_yellow = True
        
        for i in range(n):            
            g,y,r = signals[i]
            cycle = cycles[i]
            
            current_phase_time = t % cycle
            
            if not (g <= current_phase_time < g + y):
                all_yellow = False
                break
                
        if all_yellow: 
            return t + 1    
                
    return -1
    