def solution(s):
    ST = list(map(int, s.split(' ')))
    ST.sort()
    return str(ST[0])+" "+ str(ST[-1])