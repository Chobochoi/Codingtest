#include <iostream>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#define endl '\n';

using namespace std;

map<int, int> mp;
int cnt;

int N, M;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    cin >> N >> M;

    for (int i = 0; i < N + M; i++)
    {
        int c;
        cin >> c;
        mp[c]++;
    }

    for (auto i : mp)
    {
        if (i.second == 1) // value
        {
            cnt++;
        }
    }

    cout << cnt;
}

