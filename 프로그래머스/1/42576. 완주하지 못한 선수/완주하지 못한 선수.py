def solution(participant, completion):
    hash_dict = {}
    
    # 1. 참가자 명단 기록 (이름: 등장 횟수)
    for p in participant:
        if p in hash_dict:
            hash_dict[p] += 1
        else:
            hash_dict[p] = 1
            
    # 2. 완주자 명단 차감
    for c in completion:
        hash_dict[c] -= 1
        
    # 3. 완주하지 못한 선수 찾기
    for key, value in hash_dict.items():
        if value == 1:
            return key