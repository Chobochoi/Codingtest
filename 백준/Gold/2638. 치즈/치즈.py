# 백준 2638
import sys
sys.setrecursionlimit(10000)

def dfs(y, x, grid, visited, n, m):
    visited[y][x] = True
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        
        if (0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == 0):
            dfs(ny, nx, grid, visited, n, m)
            
def solve():
    n, m = map(int, input().split())
    
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
        
    time = 0
    
    while True:
        visited = [[False] * m for _ in range(n)]
        
        dfs(0, 0, grid, visited, n, m)
        
        melting = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    air_sides = 0
                    
                    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ny, nx = i + dy, j + dx
                        if(0 <= ny < n and 0 <= nx < m and visited[ny][nx]):
                            air_sides += 1
                            
                    if air_sides >= 2:
                        melting.append((i, j))            
        
        if not melting:
            break
        
        for y, x in melting:
            grid[y][x] = 0
            
        time += 1
    print(time)    
solve()                   
    