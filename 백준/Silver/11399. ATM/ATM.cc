#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using std::vector;

int main()
{
	// YAL 강의 후 필수로 추가하는 코드 3줄
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<int> v;
	int n, answer = 0;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int input = 0;
		cin >> input;

		v.push_back(input);
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++)
	{
		answer += v[i] * (n - i);
	}

	cout << answer;

	return 0;
}