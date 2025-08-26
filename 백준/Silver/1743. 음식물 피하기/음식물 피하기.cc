#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N, M, K;
int a[104][104];
int visited[104][104];

int dy[4] = { -1, 0, 1, 0 };
int dx[4] = { 0, 1, 0, -1 };

int result = 0;

int dfs(int y, int x)
{
    visited[y][x] = true;

    int token = 1;

    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
        if (a[ny][nx] == 0 || visited[ny][nx]) continue;

        token += dfs(ny, nx);
    }

    return token;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M >> K;

    for (int i = 0; i < K; i++)
    {
        int A, B;
        cin >> A >> B;

        --A;
        --B;

        a[A][B] = 1;        
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (!visited[i][j] && a[i][j] == 1)
            {
                result = max(dfs(i, j), result);
            }
        }
    }

    cout << result;
}
