#include <bits/stdc++.h>

using namespace std;

int arr[50'001];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, left = 0, right = 0, ans = 0, cnt = 0;
    cin >> n >> k;
    for(int i = 0; i < n; i++) cin >> arr[i];

    while(right < n) {
        if(cnt > k) {
            if(arr[left] % 2 == 1) cnt--;
            left++;
        } else {
            if(arr[right] % 2 == 1) cnt++;
            int len = right - left + 1 - cnt;
            if(ans < len) ans = len;
            right++;
        }
    }
    cout << ans;
    return 0;
}