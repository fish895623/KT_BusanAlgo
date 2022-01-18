#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string a, b;
    int bh, bm, bs;
    int ah, am, as;
    int ch, cm, cs;

    cin >> a >> b;

    ah = stoi(a.substr(0, 2));
    am = stoi(a.substr(3, 5));
    as = stoi(a.substr(6, 8));

    bh = stoi(b.substr(0, 2));
    bm = stoi(b.substr(3, 5));
    bs = stoi(b.substr(6, 8));

    if (bs < as) {
        bm -= 1;
        bs += 60;
    }
    if (bm < am) {
        bh -= 1;
        bm += 60;
    }
    if (bh < ah) {
        bh += 24;
    }

    ch = bh - ah;
    cm = bm - am;
    cs = bs - as;

    if (ch + cm + cs == 0) 
        ch = 24;

   printf("%02d:%02d:%02d", ch, cm, cs);
}