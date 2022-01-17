#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>
#include <cassert>
#include <map>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    vector<long long> arr(n);
    vector<int> opCnt(4);
    map<int, char> opMap = {{0, '+'}, {1, '-'}, {2, '*'}, {3, '/'}};
    string opString;

    for(int i = 0; i < n; i++) cin >> arr[i];
    for(int i = 0; i < 4; i++) {
        int x;
        cin >>x;
        while(x > 0) {
            opString.push_back(char(i) + '0');
            x-=1;
        }
    }
    vector<long long> li;
    do {
        long long sum = arr[0];
        for(int i = 0; i < opString.size(); i++){
            if (opString[i] == '0') {
                sum += arr[i + 1];
            }
            if (opString[i] == '1') {
                sum -= arr[i + 1];
            }
            if (opString[i] == '2') {
                sum *= arr[i + 1];
            }
            if (opString[i] == '3') {
                sum /= arr[i + 1];
            }
        }
        li.push_back(sum);
    } while(next_permutation(opString.begin(), opString.end()));

    cout << *max_element(li.begin(), li.end()) << '\n';
    cout << *min_element(li.begin(), li.end()) << '\n';
    return 0;
}

