#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#define endl "\n";

using namespace std;

int N;
int a[1000004];
vector<int> vec;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> a[i];        
        vec.push_back(a[i]);
    }

    sort(vec.begin(), vec.end());

    vec.erase(unique(vec.begin(), vec.end()), vec.end());

    for (int i = 0; i < N; i++)
    {
        cout << lower_bound(vec.begin(), vec.end(), a[i]) - vec.begin() << ' ';
    }

    cout << endl;

    return 0;
}