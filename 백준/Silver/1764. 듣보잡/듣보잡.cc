#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int N, M;
int result = 0;
map<string, int> mp;
string s;
set<string> ss;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    cin >> N >> M;

    for (int i = 0; i < N; i++) 
    {
        cin >> s;
        mp[s]++;
    }

    for (int i = 0; i < M; i++) 
    {
        cin >> s;
        if (mp[s] != 0) 
        {
            ss.insert(s);
        }
    }

    cout << ss.size() << '\n';
    for (auto i : ss) cout << i << '\n';

    return 0;
}

