def solution(phone_book):
    
    phone_book.sort()
    
    for start, value in zip(phone_book, phone_book[1:]):
        if value.startswith(start):
            return False

    return True
    