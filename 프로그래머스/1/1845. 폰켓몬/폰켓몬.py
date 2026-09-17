from collections import Counter

def solution(nums):
    take = len(nums) // 2
    collect = Counter(nums)
    
    kinds = len(collect)
    
    return min(take, kinds)
    

            