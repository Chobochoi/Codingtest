def solution(n, computers):
    answer = 0
    # 1. 방문 기록용 배열 생성 (모두 False로 초기화)
    visited = [False] * n

    # 2. 모든 컴퓨터(노드)를 순회
    for i in range(n):
        # 3. 아직 방문하지 않은 컴퓨터라면, 새로운 네트워크의 시작점!
        if not visited[i]:
            # 깊이 우선 탐색을 통해 이 컴퓨터와 연결된 모든 컴퓨터를 방문 처리
            dfs(n, computers, i, visited)
            # 하나의 네트워크 탐색이 끝났으므로, 네트워크 개수 1 증가
            answer += 1
            
    return answer

# 깊이 우선 탐색(DFS)을 수행하는 재귀 함수
def dfs(n, computers, start_node, visited):
    # 현재 노드를 '방문 함'으로 표시
    visited[start_node] = True
    
    # 현재 노드와 연결된 다른 모든 노드를 확인
    for j in range(n):
        # 만약 연결되어 있고(computers[start_node][j] == 1)
        # 아직 방문하지 않았다면(not visited[j])
        if computers[start_node][j] == 1 and not visited[j]:
            # 그 연결된 노드로 다시 깊이 우선 탐색을 시작 (재귀 호출)
            dfs(n, computers, j, visited)