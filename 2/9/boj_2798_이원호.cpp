#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int card[101];
int mask[101];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    int ans = 0;
    cin >> n >> m;
    for(int i = 0; i < n; i++) cin >> card[i];
    
    fill(mask + 3, mask + n, 1);
    
    do
    {
        int sum = 0;
        for(int i = 0; i < n; i++) {
            if(!mask[i])
                sum += card[i];
        }
        if(sum <= m && ans < sum)
            ans = sum;
    } while (next_permutation(mask, mask + n));
    
    cout << ans;
    return 0;
}