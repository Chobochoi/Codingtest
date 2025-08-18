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
    int result = 0;

    cin >> str;

    for (char c : str)
    {
        if (c == 'A' || c == 'B' || c == 'C')
        {
            result += 3;
        }

        else if (c == 'D' || c == 'E' || c == 'F')
        {
            result += 4;
        }

        else if (c == 'G' || c == 'H' || c == 'I')
        {
            result += 5;
        }

        else if (c == 'J' || c == 'K' || c == 'L')
        {
            result += 6;
        }

        else if (c == 'M' || c == 'N' || c == 'O')
        {
            result += 7;
        }

        else if (c == 'P' || c == 'Q' || c == 'R' || c =='S')
        {
            result += 8;
        }

        else if (c == 'T' || c == 'U' || c == 'V')
        {
            result += 9;
        }

        else if (c == 'W' || c == 'X' || c == 'Y' || c == 'Z')
        {
            result += 10;
        }
    }

    cout << result;

    return 0;  
}

