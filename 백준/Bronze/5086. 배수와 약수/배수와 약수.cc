#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string.h>
#include <stack>
#define endl "\n";

using namespace std;

int N, M;

bool check = false;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
        
    cin >> N >> M;

    while (N != 00 && M != 00)
    {
        if (M % N == 0)
        {
            cout << "factor" << endl;
        }

        else if (N % M == 0)
        {
            cout << "multiple" << endl;
        }

        else
        {
            cout << "neither" << endl;
        }
        cin >> N >> M;
    }
    return 0;
}