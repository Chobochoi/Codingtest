def solution(phone_book):
    
    phone_book.sort()
    
    for n in range(1, len(phone_book)):
        if phone_book[n].startswith(phone_book[n-1]):
            return False
        
    return True
    