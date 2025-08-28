import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)] #N+1 N+1의 2차원 배열
visited = [False] * (N+1)

def dfs(index):
    global visited
    visited[index] = True
    print(index, end = ' ')
    for next in range(1, N+1):
        if not visited[next] and graph[index][next]:
            dfs(next)
            
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)           

# 그래프 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True    
    
# dfs
dfs(V)
print() # 줄 바꿈을 위함

# bfs
visited = [False] * (N+1)
q = [V]
visited[V] = True

bfs()