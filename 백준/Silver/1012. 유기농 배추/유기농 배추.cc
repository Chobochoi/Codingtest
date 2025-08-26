#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N, M, K;
int testCase;
int a[54][54];
bool visited[54][54];

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

void dfs(int y, int x)
{
    visited[y][x] = true;

    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
        if (visited[ny][nx] || a[ny][nx] == 0) continue;

        dfs(ny, nx);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    cin >> testCase;

    while (testCase--)
    {
        cin >> M >> N >> K;

        int result = 0;

        fill(&a[0][0], &a[0][0] + 54 * 54, 0); // a[0][0] 첫~ 끝 초기화 
        fill(&visited[0][0], &visited[0][0] + 54 * 54, 0); // visited[0][0] 첫~끝 초기화

        for (int i = 0; i < K; i++)
        {
            int x, y;
            cin >> x >> y;

            a[y][x] = 1;
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (!visited[i][j] && a[i][j] == 1)
                {
                    result++;
                    dfs(i, j);
                }
            }
        }

        cout << result << endl;
    }
}
