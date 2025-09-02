import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

visited = []
while True:
    try:
        visited.append(int(input()))
    except:
        break
    
def post(start, end):
    if start > end:
        return
    mid = end + 1
    
    for i in range(start+1, end+1):
        if visited[i] > visited[start]:
            mid = i
            break
    post(start + 1, mid - 1)
    post(mid, end)
    print(visited[start])
    
post(0, len(visited)- 1)

