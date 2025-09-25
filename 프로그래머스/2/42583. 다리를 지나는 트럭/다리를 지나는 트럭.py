def solution(bridge_length, weight, truck_weights):
        
    st = [0] * bridge_length
    time = 0    
    current = 0
        
    while len(truck_weights) > 0:
        time += 1
        current = current - st.pop(0)
        
        if current + truck_weights[0] <= weight:
            current += truck_weights[0]
            st.append(truck_weights.pop(0))
        else:
            st.append(0)
            
    time += bridge_length
    
    return time
        
    
    
    