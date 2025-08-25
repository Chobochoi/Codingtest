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

int N, M;
int cnt = 0;

vector<int> vec[1004];
bool visited[1004];

void dfs(int here)
{
    visited[here] = true;

    for (int i : vec[here])
    {
        if (!visited[i])
        {
            dfs(i);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int A, B;
        cin >> A >> B;

        vec[A].push_back(B);
        vec[B].push_back(A);
    }

    for (int i = 1; i <= N; i++)
    {
        if (!visited[i])
        {
            cnt++;
            dfs(i);
        }
    }

    cout << cnt;
}
