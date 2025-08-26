# 시스템 재귀 한도 증가 (깊은 재귀 방지)
import sys
sys.setrecursionlimit(10000)

def dfs(here, depth, target, graph, visited):
    """
    DFS를 사용한 촌수 계산 함수
    
    Parameters:
    - here: 현재 위치한 사람의 번호
    - depth: 현재까지의 깊이(촌수)
    - target: 찾고자 하는 목표 사람의 번호
    - graph: 인접리스트로 표현된 가족관계 그래프
    - visited: 방문 체크 배열
    
    Returns:
    - 목표에 도달했다면 촌수, 도달하지 못했다면 -1
    """
    # 현재 사람을 방문했다고 표시
    # C++의 visited[here] = true;와 동일
    visited[here] = True
    
    # 목표 사람에 도달했다면 현재 깊이(촌수)를 반환
    # C++의 if (here == endPoint) 부분
    if here == target:
        return depth
    
    # 현재 사람과 연결된 모든 사람들을 확인
    # C++의 for (int i : vec[here])와 동일
    for next_person in graph[here]:
        # 아직 방문하지 않은 사람이라면
        if not visited[next_person]:
            # 재귀적으로 DFS 호출하여 결과 확인
            # depth + 1로 촌수 증가
            result = dfs(next_person, depth + 1, target, graph, visited)
            
            # 목표에 도달했다면 결과 반환
            # C++의 if (dfs(i, depth + 1, result)) return true; 부분
            if result != -1:
                return result
    
    # 모든 경로를 탐색해도 목표에 도달하지 못했다면 -1 반환
    # C++의 return false; 부분
    return -1

def main():
    # 입력 받기
    # C++의 cin >> N >> startPoint >> endPoint >> M;과 동일
    n = int(input())
    start_point, end_point = map(int, input().split())
    m = int(input())
    
    # 그래프 초기화 (인접리스트)
    # C++의 vector<int> vec[104];와 동일
    graph = [[] for _ in range(n + 1)]  # 1부터 n까지 사용
    
    # 방문 체크 배열 초기화
    # C++의 bool visited[104];와 동일
    visited = [False] * (n + 1)
    
    # 부모-자식 관계 입력받아 양방향 그래프 구성
    # C++의 for문과 push_back 부분
    for _ in range(m):
        a, b = map(int, input().split())
        
        # 양방향 연결 (부모↔자식 양쪽 이동 가능)
        # C++의 vec[A].push_back(B); vec[B].push_back(A);와 동일
        graph[a].append(b)
        graph[b].append(a)
    
    # DFS 실행하여 촌수 계산
    # C++의 if (dfs(startPoint, 0, result)) 부분
    result = dfs(start_point, 0, end_point, graph, visited)
    
    # 결과 출력
    # 연결되어 있으면 촌수, 연결되어 있지 않으면 -1
    print(result)

if __name__ == "__main__":
    main()