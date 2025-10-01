def solution(left, right):
    
    total = 0

    st = []

    while left < right+1:
        for i in range(1, left+1):
            if left % i == 0:
                st.append(i)     

        if len(st) % 2 == 0:
            total += left
            left += 1
            st = []
        else:
            total -= left
            left += 1
            st = []

    return total