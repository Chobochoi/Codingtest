#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N = 9;
vector<int> vec;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 0; i < N; i++)
    {
        int tall;
        cin >> tall;

        vec.push_back(tall);
    }


    // next_permutation을 쓸 때에는 sort 필요
    sort(vec.begin(), vec.end());

    while (next_permutation(vec.begin(), vec.end()))
    {
        int result = 0;

        for (int i = 0; i < 7; i++)
        {
            result += vec[i];
        }

        if (result == 100)
        {
            break;
        }
    }

    vector<int> solution;

    for (int i = 0; i < 7; i++)
    {
        solution.push_back(vec[i]);
    }

    sort(solution.begin(), solution.end());

    for (int i : solution)
    {
        cout << i << endl;
    }
}
