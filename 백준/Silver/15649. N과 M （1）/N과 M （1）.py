y, x = map(int, input().split())

st = []

def check():
    if len(st) == x:
        print(' '.join(map(str, st)))
        
    for i in range(1, y+1):
        if i not in st:
            st.append(i)
            check()
            st.pop()
            
check()