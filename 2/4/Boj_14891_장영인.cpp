#include<iostream>
#include<algorithm>
#include<deque>
using namespace std;

deque<int> q1, q2, q3, q4;

void rotate(deque<int>& q, int dir) {
    int s = 0;
    if (dir == -1) {
        s = q.front();
        q.pop_front();
        q.push_back(s);
    }
    if (dir == 1) {
        s = q.back();
        q.pop_back();
        q.push_front(s);
    }
}

void rotation(int num, int dir) {

    pair<int, int>c1, c2, c3, c4;
    c1 = { 0,q1[2] };
    c2 = { q2[6],q2[2] };
    c3 = { q3[6],q3[2] };
    c4 = { q4[6],q4[2] };

    if (num == 1){
        rotate(q1, dir);
        if (c1.second != c2.first) {
            rotate(q2, -dir);
            if (c2.second != c3.first) {
                rotate(q3, dir);
                if (c3.second != c4.first)
                    rotate(q4, -dir);
            }
        }
    }

    if (num == 2) {
        rotate(q2, dir);
        if (c2.first != c1.second) 
            rotate(q1, -dir);
        if (c2.second != c3.first) {
            rotate(q3, -dir);
            if (c3.second != c4.first)
                rotate(q4, dir);
        }
    }

    if (num == 3) {
        rotate(q3, dir);
        if (c3.first != c2.second) {
            rotate(q2, -dir);
            if (c2.first != c1.second)
                rotate(q1, dir);
        }
        if (c3.second != c4.first) 
            rotate(q4, -dir);
    }

    if (num == 4) {
        rotate(q4, dir);
        if (c4.first != c3.second) {
            rotate(q3, -dir);
            if (c3.first!= c2.second) {
                rotate(q2, dir);
                if (c2.first != c1.second)
                    rotate(q1, -dir);
            }
        }
    }
}

int main() {
    int k, num, dir, sum = 0;
    char state;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 8; j++) {
            cin >> state;
            if (i == 0) q1.push_back(state-'0');
            else if (i == 1) q2.push_back(state-'0');
            else if (i == 2) q3.push_back(state - '0');
            else if (i == 3) q4.push_back(state - '0');
        }
    }

    cin >> k;
    for (int i = 0; i < k; i++) {
        cin >> num >> dir;
        rotation(num, dir);
    }

    if (q1[0] == 1) sum += 1;
    if (q2[0] == 1) sum += 2;
    if (q3[0] == 1) sum += 4;
    if (q4[0] == 1) sum += 8;

    cout << sum;

}