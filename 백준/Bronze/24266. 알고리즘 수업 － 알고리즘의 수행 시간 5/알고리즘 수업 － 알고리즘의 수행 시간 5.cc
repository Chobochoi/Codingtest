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

	cout << n * n * n << "\n" << 3; 
}