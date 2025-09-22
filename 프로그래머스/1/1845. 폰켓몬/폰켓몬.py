def solution(nums):
    
    length = len(nums)/2
    
    set_nums = set(nums)
    list_nums = list(set_nums)
    
    if len(list_nums) <= length:
        return len(list_nums)
    else:
        return length
    
        
    
        