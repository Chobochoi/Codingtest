#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int num, N;
vector<int> vec;


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> num;
		vec.push_back(num);
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < N; i++)
	{
		cout << vec[i] << "\n";
	}

	return 0;		
}
