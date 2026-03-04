# 260304
# 해당 문제의 가장 중요한 요소 집합(Set)
# Set은 중복을 제거할 때 사용하는 자료구조
def solution(nums):
    
    max_select = len(nums) // 2
    
    kind_total = len(set(nums))
    
    if max_select >= kind_total :
        return kind_total
    else:
        return max_select
    
    
            