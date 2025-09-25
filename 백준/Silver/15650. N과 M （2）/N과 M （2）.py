N, M = map(int, input().split())
st = []

def backtracking(start):
    if len(st) == M:
        print(' '.join(map(str, st)))
        
    for i in range(start, N+1):
        if i not in st:
            st.append(i)
            backtracking(i+1)
            st.pop()
            
backtracking(1)