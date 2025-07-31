#include <iostream>
#include <cmath>
#include <map>

using namespace std;

int N, M;

map<int, int> mp;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // map O(N*logN)
    // 시간 복잡도 1800만 정도
    //int value = 500000 * log2(500000) * 2;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int input;

        cin >> input;

        mp[input]++;
    }

    cin >> M;

    for (int i = 0; i < M; i++)
    {
        int input;

        cin >> input;

        if (mp[input])
        {
            cout << "1 ";
        }

        else cout << "0 ";
    }

}

