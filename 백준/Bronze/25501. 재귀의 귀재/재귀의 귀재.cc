#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string.h>
#include <stack>
#define endl "\n";

using namespace std;

int cnt = 0;

int recursion(const char* s, int l, int r) 
{
    cnt++;
    if (l >= r) return 1;
    else if (s[l] != s[r]) return 0;
    else return recursion(s, l + 1, r - 1);
}

int isPalindrome(const char* s) 
{
    return recursion(s, 0, strlen(s) - 1);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    string str;
    
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cnt = 0;
        cin >> str;
        cout << isPalindrome(str.c_str()) << " " << cnt << endl;        
    }

    return 0;
}
