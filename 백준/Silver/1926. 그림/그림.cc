#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int a[504][504];
int visited[504][504];

int N, M;
int dy[4] = { -1, 0, 1, 0 };
int dx[4] = { 0, 1, 0, -1 };

int maxToken = 0;
int cnt = 0;

int dfs(int y, int x)
{
    visited[y][x] = true;

    int token = 1;

    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
        if (visited[ny][nx] || a[ny][nx] == 0) continue;

        token += dfs(ny, nx);
    }

    return token;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> a[i][j];
        }
    }  

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (!visited[i][j] && a[i][j] == 1)
            {
                cnt++;
                maxToken = max(dfs(i, j), maxToken);
            }
        }
    }

    cout << cnt << endl;
    cout << maxToken << endl;
}
