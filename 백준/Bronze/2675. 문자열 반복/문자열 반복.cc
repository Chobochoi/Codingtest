#include <iostream>

using namespace std;

int main()
{
	int T, R;
	string S;

	cin >> T;

	while (T--)
	{
		cin >> R >> S;

		for (int i = 0; i < S.length(); i++)
		{
			for (int k = 0; k < R; k++)
			{
				cout << S[i];
			}
		}
		cout << "\n";
	}
	return 0;
}