#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T, C;
    int coin[4] = { 25, 10, 5, 1 };
    
    cin >> T;

    while (T--)
    {
        cin >> C;
        
        for (int i = 0; i < 4; i++)
        {
            cout << C / coin[i] << ' ';

            C %= coin[i];
        }

        cout << '\n';
    }

    return 0;
}