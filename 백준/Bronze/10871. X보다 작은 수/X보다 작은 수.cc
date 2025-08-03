#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int N, X;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> X;

	for (int i = 0; i < N; i++)
	{
		int input;
		cin >> input;

		if (input < X)
		{
			cout << input << " ";
		}		
	}
}