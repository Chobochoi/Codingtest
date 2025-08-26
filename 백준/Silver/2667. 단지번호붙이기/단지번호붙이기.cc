#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int a[30][30];
bool visited[30][30];

int N;

vector<int> vec;
int dy[4] = { -1, 0, 1,0 };
int dx[4] = { 0, 1, 0, -1 };

int cnt = 0;

int dfs(int y, int x)
{
    visited[y][x] = true;

    int token = 1;

    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
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

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;
        
        for (int j = 0; j < N; j++)
        {
            a[i][j] = str[j]- '0';
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!visited[i][j] && a[i][j] == 1)
            {
                cnt++;
                vec.push_back(dfs(i, j));
            }
        }
    }

    cout << cnt << endl;

    sort(vec.begin(), vec.end());

    for (int i : vec)
    {
        cout << i << endl;
    }

}
