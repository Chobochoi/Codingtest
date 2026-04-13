#260413
def solution(n, lost, reserve):
    
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
        
    for l in sorted(real_lost):
    
        if l - 1 in real_reserve:
            real_reserve.remove(l - 1)
        
        elif l + 1 in real_reserve:
            real_reserve.remove(l + 1)
        
        else:
            n -= 1 
            
    return n