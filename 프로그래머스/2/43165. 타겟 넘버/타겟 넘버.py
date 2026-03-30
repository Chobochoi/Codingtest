#260330
def solution(numbers, target):    
    def dfs(total, index):
        if index == len(numbers):
            if total == target:
                return 1
            else:
                return 0
                
        return dfs(total + numbers[index], index + 1) + dfs(total - numbers[index], index + 1)
        
    return dfs(0, 0)
