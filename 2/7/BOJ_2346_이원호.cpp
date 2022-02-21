#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    deque<pair<int, int>> dq;
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        dq.push_back({i, x});
    }

    while(!dq.empty())
    {
        int idx = dq.front().first;
        int rotate = dq.front().second;
        dq.pop_front();

        rotate = rotate > 0 ? rotate - 1 : rotate;

        if(rotate > 0)
        {
            while(rotate > 0)
            {
                dq.push_back(dq.front());
                dq.pop_front();
                rotate--;
            }
        }
        else 
        {
            while(rotate < 0) {
                dq.push_front(dq.back());
                dq.pop_back();
                rotate++;
            }
        }
        cout << idx << ' ';
    }
    return 0;
}
