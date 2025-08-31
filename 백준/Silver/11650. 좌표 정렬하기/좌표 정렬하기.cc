#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N;
int x, y;
vector<pair<int, int>> vec;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> x >> y;

        vec.push_back({ x, y });
    }

    sort(vec.begin(), vec.end());

    for (int i = 0; i < N; i++)
    {
        cout << vec[i].first << ' ' << vec[i].second << endl;
    }

    return 0;
}
