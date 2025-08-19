#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

string alpha = "abcdefghijklmnopqrstuvwxyz";
string str;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);          

    cin >> str;

    for (int i = 0; i < alpha.size(); i++)
    {
        // 만약 맞으면 인덱스 번호를 알려줌
        // 없으면 string::npos = -1
        // u longlong 형식임 << 이걸 변환 해주면 됨 int 형으로
        cout << (int)str.find(alpha[i]) << " "; 
    }
}

