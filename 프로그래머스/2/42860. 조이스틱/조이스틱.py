#260415
def solution(name):
    answer = 0
    n = len(name)
    
    min_move = n - 1 
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
                
        min_move = min(min_move,i * 2 + n - next_i, i + 2 * (n - next_i)) 
    
    return answer + min_move