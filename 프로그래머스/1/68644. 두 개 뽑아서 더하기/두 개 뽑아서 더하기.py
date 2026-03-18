#260318
def solution(numbers):
    result = []
            
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_two = numbers[i] + numbers[j]            
            result.append(sum_two)
            
    final = list(set(result))
    final.sort()
    
    return final