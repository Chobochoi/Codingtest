#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int number[5];
int result;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for (int i = 0; i < 5; i++)
	{
		cin >> number[i];
		result += number[i];
	}
	
	sort(number, number + 5);

	cout << result / 5 << "\n";
	cout << number[2];
}