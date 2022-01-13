#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> arr(n);
    for(int i = 0; i < n; i++) cin >> arr[i]; 

    sort(arr.begin(), arr.end());

    int left = 0, right = n - 1;
    long long ansLeft = 0, ansRight = 0;

    long long minimum = 20'000'000'001;

    while(left < right)
    {
        long long sum = arr[left] + arr[right];

        if(minimum > (sum < 0 ? -sum : sum)) {
            minimum = (sum < 0 ? -sum : sum);
            ansLeft = arr[left];
            ansRight = arr[right];
        }
        if(sum < 0) left++;
        if(sum == 0) break;
        if(sum > 0) right--;
    }
    cout << ansLeft << ' ' << ansRight;
    return 0;
}
