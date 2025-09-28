def solution(n):
    
    st = [] 
    
    for i in range(1, n+1):
        if n % i == 0:
            st.append(i)
            
    return sum(st)