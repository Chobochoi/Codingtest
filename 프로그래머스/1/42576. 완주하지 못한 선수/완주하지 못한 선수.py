def solution(participant, completion):
    
    dic = {}
    
    for name in participant:
        dic[name] = dic.get(name, 0) + 1
        
    for name in completion:
        dic[name] = dic.get(name, 0) - 1
        
    for name in dic:
        if dic[name] != 0:
            return name
            