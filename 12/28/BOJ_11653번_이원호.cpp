#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>
#include <cmath>
#include <queue>
#include <list>
#include <stack>
#include <stdio.h>
#include <set>
#include <functional>

using namespace std;

vector<int> factor(int n)
{
    vector<int> ret;
    
    for (int d = 2; n > 1; d++) {
        while(n % d == 0) {
            n /= d;
            ret.push_back(d);
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector<int> ret = factor(n);

    for(auto val : ret) cout << val << '\n';
    
    return 0;
}

