#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<long long> arr(n);
    int max_len = 0;
    
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    long long left = 1, right = *max_element(arr.begin(), arr.end());

    while (left <= right)
    {
        long long mid = (left + right) / 2;
        int cnt = 0;
        
        for (auto val : arr)
            cnt += val / mid;
        
        if (cnt >= m) {
            max_len = mid;
            left = mid + 1;
        }
        else
            right = mid - 1;
    }
    cout << max_len;
    return 0;
}
