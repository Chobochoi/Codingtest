# 260302
# Python 내재함수 Counter 활용.
import collections

def solution(participant, completion):
    # 1. 참가자와 완주자의 빈도수 차이를 계산하여 완주하지 못한 선수(1명)를 남김
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    # 2. 남은 1명의 데이터에서 Key값만 추출하여 리스트로 변환 후 문자열 반환
    return list(answer.keys())[0]