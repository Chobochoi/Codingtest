#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

string A, B;


int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);          

    cin >> A >> B;

    reverse(&A[0], &A[A.size()]);
    reverse(&B[0], &B[B.size()]);

    if (A < B)
    {
        cout << B;
    }

    else
    {
        cout << A;
    }
}

