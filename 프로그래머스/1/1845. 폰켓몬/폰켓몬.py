def solution(nums):
    max_take = len(nums)//2
    
    arr = []
    
    for n in nums:
        if n not in arr:
            arr.append(n)
            
    answer = min(len(arr), max_take)           

    return answer
      