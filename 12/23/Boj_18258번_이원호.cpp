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
    int n;
    cin >> n;
    queue<int> q;
    while (n--)
    {
        string s;
        cin >> s;
        if (s == "push")
        {
            int x;
            cin >> x;
            q.push(x);
            continue;
        }
        if (s == "pop")
        {
            if(q.empty()) cout << -1 <<'\n';
            else {cout << q.front() << '\n'; q.pop();}
            continue;
        }
        if (s == "size")
        {
            cout << q.size() << '\n';
            continue;
        }
        if (s == "empty")
        {
            if(q.empty()) cout << 1 << '\n';
            else cout << 0 << '\n';
            continue;
        }
        if (s == "front")
        {
            if(q.empty()) cout << -1 << '\n';
            else cout << q.front() << '\n';
            continue;
        }
        if (s == "back")
        {
            if(q.empty()) cout << -1 << '\n';
            else cout << q.back() << '\n';
            continue;
        }
    }
    return 0;
}