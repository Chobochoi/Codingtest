#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

// DFS : Depth First Search = 깊이 우선 탐색
/*
* 목표가 깊은 단계에 있을 때 효율적
* 모든 경우의 수 깊히 파고 들 때
* 시간복잡도는 O(V+E) vertex (정점) + edge (간선)
*/

using namespace std;

vector<int> vec[100004];
int parent[100004];
bool visited[100004];

int N;

void dfs(int here)
{
    visited[here] = true;

    for (int i : vec[here]) // here이 부모, i가 자식
    {
        if (!visited[i])
        {
            parent[i] = here;
            dfs(i);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    for (int i = 0; i < N - 1; i++)
    {
        int A, B; // 연결하는 선
        cin >> A >> B;

        vec[A].push_back(B);
        vec[B].push_back(A);

    }

    dfs(1); // 트리는 전부 다 연결이 되어있어서 1번만 돈다.

    for (int i = 2; i <= N; i++)
    {
        cout << parent[i] << endl;
    }    
}
