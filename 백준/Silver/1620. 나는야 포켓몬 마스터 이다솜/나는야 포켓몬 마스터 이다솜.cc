#include <iostream>
#include <cmath>
#include <map>
#define endl '\n';

/* 1602번
*  번호에다가 이름을, 이름에다가 번호를 삽입 두 번 필요
*  (2*100000) * log2(100000) + (100000 * log2(100000));
*  시간 복잡도 nlog + mlogn
*/

using namespace std;

int N, M;
map<string, int> mp;
map<int, string> mp2;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        string s;
        cin >> s;

        mp[s] = i;
        mp2[i] = s;
    }

    for (int i = 0; i < M; i++)
    {
        string s;
        cin >> s;

        // 아토이 (아스키코드를 int형으로 바꿔준다.) 앞에 숫자가 있으면 숫자만 뽑고, 문자가 있으면 0 반환
        if (int a = atoi(s.c_str()))
        {
            // 숫자다
            cout << mp2[a] << endl;
        }

        else
        {
            // 문자다
            cout << mp[s] << endl;
        }
    }
}
