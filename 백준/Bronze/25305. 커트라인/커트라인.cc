#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int N, k;
int x[1000];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> k;

	for (int i = 0; i < N; i++)
	{
		cin >> x[i];
	}

	sort(x, x+N, greater<>());

	cout << x[k-1];
}