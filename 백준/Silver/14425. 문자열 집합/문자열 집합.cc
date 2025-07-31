#include <iostream>
#include <map>

using namespace std;


int main()
{
	// YAL 강의 후 필수로 추가하는 코드 3줄
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, result = 0;
	string str;
	map<string, bool> mp;

	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		cin >> str;
		mp.insert(pair<string, bool>(str, true));
	}

	for (int j = 0; j < M; j++)
	{
		cin >> str;
		if (mp[str] == true)
		{
			result++;
		}
	}
	cout << result;
}