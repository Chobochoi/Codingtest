def solution(s):
    if len(s) in (4,6):
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False

        