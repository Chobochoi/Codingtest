#include <iostream>

using namespace std;

int main()
{
	string s;
	int n;
	int result = 0;

	cin >> n >> s;

	for (int i = 0; i < n; i++)
	{
		result += s[i] - '0';
	}

	cout << result;
}