#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int num, N;
int arr[10001] = { 0 };


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> num;
		arr[num]++;
	}

	for (int i = 1; i < 10001; i++)
	{
		for (int j = 0; j < arr[i]; j++)
		{
			cout << i << '\n';
		}
	}
	
	return 0;
}
