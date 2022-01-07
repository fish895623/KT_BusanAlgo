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
#include <string>

using namespace std;

int sushi[3'000'001];
int table[3001];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d, k, c;
    cin >> n >> d >> k >> c;
    
    for(int i = 0; i < n; i++)
        cin >> sushi[i];
    
    int max = 0;
    int cnt = 0;

    int start = 0;
    int end = k - 1;
    
    table[c] = 1;

    for(int i = start; i <= end; i++) {
        table[sushi[i]] += 1;
        if(table[sushi[i]] == 1) cnt += 1;
    }
    max = cnt;

    for(int i = 0; i < n - 1; i++) {
        table[sushi[start]] -= 1;
        if(table[sushi[start]] == 0) cnt -= 1;

        start += 1;
        end = (end + 1) % n;
        
        table[sushi[end]] += 1;
        if(table[sushi[end]] == 1) cnt += 1;

        if (max < cnt) max = cnt;
    }
    
    cout << max + 1;
    return 0;
}
