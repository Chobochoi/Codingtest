def solution(arr):
    
    st = []
    st.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            st.append(arr[i])    
                
    return st