// 백준 24267번
#include <iostream>

using namespace std;

int main()
{
	// YAL 강의 후 필수로 추가하는 코드 3줄
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long n;

	cin >> n; 

	cout << ((n-2) * (n-1) * n)/6 << "\n" << 3; 
}