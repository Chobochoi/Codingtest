# 260401
def solution(nums):
    
    max_select = len(nums) // 2
    
    kind_total = len(set(nums))
    
    if max_select >= kind_total :
        return kind_total
    else:
        return max_select
    
    
            