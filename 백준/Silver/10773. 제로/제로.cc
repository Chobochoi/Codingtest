#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int K, N, stack_size;
int result = 0;
stack<int> stk;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);          

    cin >> K;

    for (int i = 0; i < K; i++)
    {
        cin >> N;

        if (N == 0)
        {
            stk.pop();
        }

        else
        {
            stk.push(N);
        }
    }

    stack_size = stk.size();

    for (int i = 0; i < stack_size; i++)
    {
        result += stk.top();
        stk.pop();
    }

    cout << result;

    return 0;  
}

