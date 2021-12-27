#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>
#include <cmath>
#include <queue>
#include <list>
#include <stack>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    stack<int> stck;
    string ans;
    int n;
    int cnt = 1;

    cin >> n;

    while (n--)
    {
        int x;
        cin >> x;
        while(x >= cnt) {
            stck.push(cnt++);
            ans += "+\n";
        }
        if(stck.top() != x)
        {
            cout << "NO\n";
            return 0;
        }
        stck.pop();
        ans += "-\n";
    }
    cout << ans;
    return 0;
}
