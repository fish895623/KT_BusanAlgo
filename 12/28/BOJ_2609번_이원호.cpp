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


int gcd(int a, int b)
{
    if (b > a) return gcd(b, a);
    if (a % b == 0) return b;
    else return gcd(b, a % b);
}


int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y;
    cin >> x >> y;
    int g = gcd(x, y);
    int r = x / g * y;
    cout << g << '\n' << r;
    return 0;
}


