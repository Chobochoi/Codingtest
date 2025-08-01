#include <iostream>
#include <cmath>
#include <map>

#define endl '\n';

using namespace std;

int N;
string s, check;

map<string, bool> mp;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> s >> check;

        if (check == "enter")
        {
            mp[s] = true;
        }

        else if (check == "leave")
        {
            mp[s] = false;
        }
    }

    for (auto it = mp.rbegin(); it != mp.rend(); it++) // 거꾸로 순회시키기 위함
    {
        if (it->second) // second는 value 값
        {
            cout << it->first << endl;
        }
    }
}

