def solution(s):
    ST = []
    for i in s:
        if i == '(':
            ST.append('(')
        else :
            if ST == []:
                return False
            else:
                ST.pop()
                
    return ST==[]
        
        