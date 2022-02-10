#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define G 'X'
#define S '.'

const int dy[] = {0, 0, -1, 1};
const int dx[] = {-1, 1, 0, 0};

queue<pair<int, int>> groundQue;
queue<pair<int, int>> sinkQue;

string ground[10];

bool getArea(int y, int x, int sizeY, int sizeX)
{
    int cnt = 4;
    for(int dir = 0; dir < 4; dir++)
    {
        int ay = y + dy[dir];
        int ax = x + dx[dir];
        if(ay < 0 || ax < 0 || ay >= sizeY || ax >= sizeX) continue;
        if(ground[ay][ax] == G) cnt -= 1;
    }
    return cnt >= 3;
}

vector<int> resize(int sizeY, int sizeX)
{
    bool valid = true;
    int startY = 0, startX = 0, endY = sizeY-1, endX = sizeX-1;
    vector<int> ret;

    valid = true;
    while(true)
    {

        for(int i = 0; i < sizeX; i++)
            if(ground[startY][i] == G) {
                valid=false;
                break;
            }
        if(valid) startY++;
        else break;
    }

    valid = true;
    while(true)
    {

        for(int i = 0; i < sizeX; i++)
            if(ground[endY][i] == G) {
                valid=false;
                break;
            }
        if(valid) endY--;
        else break;
    }

    valid = true;
    while(true)
    {

        for(int i = 0; i < sizeY; i++)
            if(ground[i][startX] == G) {
                valid=false;
                break;
            }
        if(valid) startX++;
        else break;
    }

    valid = true;
    while(true)
    {

        for(int i = 0; i < sizeY; i++)
            if(ground[i][endX] == G) {
                valid=false;
                break;
            }
        if(valid) endX--;
        else break;
    }
    
    ret.push_back(startY);
    ret.push_back(endY);
    ret.push_back(startX);
    ret.push_back(endX);

    return ret;
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for(int i = 0; i < n; i++) cin >> ground[i];
    
    for(int y = 0; y < n; y++)
        for(int x = 0; x < m; x++)
            if(ground[y][x] == 'X')
                groundQue.push({y, x});
    
    while(!groundQue.empty())
    {
        pair<int, int> curr = groundQue.front();
        groundQue.pop();

        int y = curr.first;
        int x = curr.second;
        if(getArea(y, x, n, m)) sinkQue.push({y, x});
    }
    while(!sinkQue.empty())
    {
        pair<int, int> curr = sinkQue.front();
        sinkQue.pop();
        ground[curr.first][curr.second] = S;
    }  

    vector<int> size;
    size = resize(n, m);
    for(int i = size[0]; i <= size[1]; i++) {
        for(int j = size[2]; j <= size[3]; j++) {
            cout << ground[i][j];
        }
        cout << '\n';
    }

    return 0;
}