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

int rope[100'001];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
	cout.tie(nullptr);

    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++)
        cin >> rope[i];
    
    int maximum = 0;
    sort(rope, rope + n);
    for(int i = 0; i < n; i++) 
        maximum = max(maximum, rope[i] * (n - i));

    cout << maximum;
    return 0;
}
