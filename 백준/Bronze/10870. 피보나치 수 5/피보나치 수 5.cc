#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N;
int result = 0;
int temp1 = 0; // 첫번째 수
int temp2 = 1; // 두번째 수

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;   
    
    for (int i = 1; i <= N; i++)
    {               
        result = temp1 + temp2;
        temp2 = temp1;
        temp1 = result;
    }
    cout << result;

    return 0;
}