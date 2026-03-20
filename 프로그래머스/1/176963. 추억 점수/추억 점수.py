#263020
def solution(name, yearning, photo):
    answer = []
    
    hash_map = {}
    
    for n, y in zip(name, yearning):
        hash_map[n] = y
        
    for p in photo:
        score = 0
        
        for i in p:
            if i in hash_map:
                score += hash_map[i]
                
        answer.append(score)
        
    return answer