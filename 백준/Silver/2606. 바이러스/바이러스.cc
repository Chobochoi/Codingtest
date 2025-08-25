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

vector<int> vec[104];
bool visited[104];

int N, M;

int cnt;

void dfs(int here)
{
    // 어느 부분에서 시작하는지 알 수 있음.
    visited[here] = true;

    for (int i : vec[here])
    {
        if (!visited[i])
        {
            cnt++;
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

    dfs(1);

    cout << cnt;
}
