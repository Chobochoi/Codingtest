#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

string strN;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> strN;

	sort(strN.begin(), strN.end(), greater<char>());

	cout << strN;
}
