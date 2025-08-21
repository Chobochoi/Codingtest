#include <iostream>
#define MAX 100

using namespace std;

int main()
{
	int n, m, sum, goal = 0;
	int min = 9999999;
	int arr[MAX];

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < n - 2; i++)			// 중복 방지를 위함.
		for (int j = i+1; j < n - 1; j++)	// j는 i 이후부터
			for (int k = j+1; k < n; k++)	// k는 j 이후부터
			{
				sum = arr[i] + arr[j] + arr[k];

				if (m - sum < min && m - sum >= 0)
				{
					min = m - sum;
					goal = sum;
				}
			}
			cout << goal;	
}