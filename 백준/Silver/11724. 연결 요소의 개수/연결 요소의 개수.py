N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    

def dfs(start):
    visited[start] = True
    
    for value in graph[start]:
        if not visited[value]:
            dfs(value)
        
answer = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1
        
print(answer)