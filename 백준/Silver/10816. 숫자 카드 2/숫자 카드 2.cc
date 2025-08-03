#include <iostream>
#include <cmath>
#include <map>
#define endl '\n';

using namespace std;

int N, M;

map<int, int> mp;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    cin >> N;
    
    for (int i = 0; i < N; i++)
    {
        int c;
        cin >> c;

        mp[c]++;
    }

    cin >> M;

    for (int i = 0; i < M; i++)
    {
        int c;
        cin >> c;
        cout << mp[c] << " ";
    }
}

