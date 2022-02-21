#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define MAX 0xfffff

const int dy[] = {0, 0, -1, 1};
const int dx[] = {-1, 1, 0, 0};

int floor[10][10];
int mask[101];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int ans = MAX;
    cin >> n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            cin >> floor[i][j];
    fill(mask + 3, mask + n * n, 1);
    do
    {
        bool isValid = true;
        bool validMap[10][10] = {false};
        int sum = 0;
        for(int i = 0; i < n * n; i++)
            if(!mask[i]) {
                int y = i / n;
                int x = i % n;
                if(validMap[y][x]) {
                    isValid=false;
                    break;
                }
                validMap[y][x] = true;
                sum += floor[y][x];

                for(int dir = 0; dir < 4; dir++)
                {
                    int ay = y + dy[dir];
                    int ax = x + dx[dir];

                    if(ay < 0 || ax < 0 || ay >= n || ax >= n || validMap[ay][ax]) {
                        isValid=false;
                        break;
                    }
                    validMap[ay][ax] = true;
                    sum += floor[ay][ax];
                }
            }
        if(!isValid) continue;
        if(sum < ans) 
            ans = sum;
    } while (next_permutation(mask, mask + n * n));
    cout << ans;
    return 0;
}