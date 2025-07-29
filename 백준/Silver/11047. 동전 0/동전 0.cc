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

	int a[11];
	int N, K;
	cin >> N >> K;

	for (int i = 0; i < N; i++)
	{
		cin >> a[i];
	}

	int result = 0;

	for (int i = N - 1; i >= 0; i--)
	{
		result += K / a[i];
		K = K % a[i];
	}

	cout << result << '\n';
}