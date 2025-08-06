#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int N;
string strN[20000];

int compare(string a, string b)
{
	if (a.length() == b.length())
	{
		return a < b;
	}

	else
	{
		return a.length() < b.length();
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> strN[i];
	}

	sort(strN, strN + N, compare);

	for (int i = 0; i < N; i++)
	{
		
		if (i >= 1 && (strN[i] == strN[i - 1]))
		{
			continue;
		}

		cout << strN[i] << "\n";
	}

	return 0;

}
