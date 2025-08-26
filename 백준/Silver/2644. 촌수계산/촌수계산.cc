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
int startPoint, endPoint;

vector<int> vec[104];

bool visited[104];

bool dfs(int here, int depth, int& result)
{
    visited[here] = true;

    if (here == endPoint)
    {
        result = depth;

        return true;
    }

    for (int i : vec[here])
    {
        if (!visited[i])
        {
            if (dfs(i, depth + 1, result))
            {
                return true;
            }
        }
    }

    return false;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> startPoint >> endPoint >> M;

    for (int i = 0; i < M; i++)
    {
        int A, B;

        cin >> A >> B;

        vec[A].push_back(B);
        vec[B].push_back(A);

    }
    
    int result = -1;

    if (dfs(startPoint, 0, result))
    {
        cout << result;
    }

    else
    {
        cout << -1;
    }
}
