// 백준 24313번
#include <iostream>

using namespace std;

int main()
{
	// YAL 강의 후 필수로 추가하는 코드 3줄
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a0, a1; 
	int c;
	int N;

	cin >> a1 >> a0;
	cin >> c;
	cin >> N;

	int fn = a1 * N + a0;
	int gn = c * N;

	if (fn <= gn && a1 <=c)
	{
		cout << "1";
	}

	else cout << "0";
}