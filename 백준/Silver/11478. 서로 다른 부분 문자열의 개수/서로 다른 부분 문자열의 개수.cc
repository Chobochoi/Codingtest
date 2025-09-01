#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#include <set>
#define endl "\n";

using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);   
    
    string str1;
    cin >> str1;

    set<string> setAlpha;

    string str2 = "";

    for (int i = 0; i < str1.size(); i++)
    {
        for (int j = i; j < str1.size(); j++)
        {
            str2 += str1[j];
            setAlpha.insert(str2);
        }
        str2 = "";
    }
    cout << setAlpha.size();
}