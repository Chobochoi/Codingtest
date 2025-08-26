#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N;
int a[104][104];
int visited[104][104];

int dy[4] = { -1, 0 ,1 ,0 };
int dx[4] = { 0, 1, 0, -1 };

int maxNum;
int result = 1;

void dfs(int y, int x, int depth)
{
    visited[y][x] = true;

    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
        if (a[ny][nx] <= depth || visited[ny][nx]) continue;

        dfs(ny, nx, depth);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);        

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> a[i][j];

            maxNum = max(maxNum, a[i][j]);
        }
    }

    for (int k = 1; k <= maxNum; k++)
    {
        int cnt = 0;
        fill(&visited[0][0], &visited[0][0] + 104 * 104, 0);

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (!visited[i][j] && a[i][j] > k)
                {
                    dfs(i, j, k);
                    cnt++;
                }
            }
        }

        result = max(result, cnt);
    }

    cout << result;
    
}
