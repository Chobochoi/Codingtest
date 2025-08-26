#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N, M;
int a[104][104];
int visited[104][104];

int dy[4] = { -1 , 0, 1 ,0 };
int dx[4] = { 0, 1, 0,-1 };

int cnt = 0;

void dfs(int y, int x)
{
    visited[y][x] = 1;

    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
        if (visited[ny][nx] || a[ny][nx] == 1) continue;

        dfs(ny, nx);
    }
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

    while (true)
    {
        fill(&visited[0][0], &visited[0][0] + 104 * 104, 0);

        dfs(0, 0);

        vector<pair<int, int>> meltingCheese;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (a[i][j] == 1)
                {
                    int air = 0;

                    for (int k = 0; k < 4; k++)
                    {
                        int ny = i + dy[k];
                        int nx = j + dx[k];

                        if (visited[ny][nx] == 1)
                        {
                            air++;
                        }
                    }

                    if (air >= 2)
                    {
                        meltingCheese.push_back({ i, j });
                    }
                }
            }
        }

        if (meltingCheese.empty())
        {
            break;
        }

        cnt++;

        for (pair<int, int> pos : meltingCheese)
        {
            a[pos.first][pos.second] = 0;
        }
    }

    cout << cnt << endl;
}
