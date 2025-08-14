#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

using namespace std;


int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);    

    string str;
    int result = 1;

    getline(cin, str);

    int strLength = str.length();

    for(int i =0; i < strLength; i++)
    {
        if (str[i] == ' ')
        {
            result++;
        }
    }

    if (str[0] == ' ')
    {
        result--;
    }

    if (str[strLength - 1] == ' ')
    {
        result--;
    }

    cout << result;

    return 0;
}

