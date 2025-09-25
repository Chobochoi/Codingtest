from itertools import combinations

def solution(nums):
    
    st = []
    
    pick = len(nums)/2
        
    for num in nums:
        if num not in st:
            st.append(num)
            
    st.sort()
    
    if len(st) >= pick:
        return pick
    else:
        return len(st)
            