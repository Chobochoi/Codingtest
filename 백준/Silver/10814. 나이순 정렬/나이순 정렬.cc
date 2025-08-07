#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

bool compare(pair<int, string> a, pair<int, string> b)
{
	return a.first < b.first;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	pair<int, string> temp;
	vector<pair<int, string>> vec;

	int N;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> temp.first >> temp.second;

		vec.push_back(temp);
	}

	stable_sort(vec.begin(), vec.end(), compare);

	for (int i = 0; i < N; i++)
	{
		cout << vec[i].first << " " << vec[i].second << "\n";
	}
}