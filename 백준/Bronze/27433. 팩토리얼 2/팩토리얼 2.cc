#include <iostream>
//#include <algorithm>
//#include <map>
//#include <vector>
//#include <string>
//#include <stack>
#define endl "\n";

using namespace std;

int N;
long long int result = 1;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;   
    
    for (int i = 1; i <= N; i++)
    {        
        result *= i;
    }

    cout << result;

    return 0;
}
