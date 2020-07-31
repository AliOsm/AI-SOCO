#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;

int main() {
    ios::sync_with_stdio(false);
    int q; cin >> q;
    int x,y,h,w;
    x = y = h = w = 0;
    char oper;
    while(q--) {
        cin >> oper >> h >> w;
        if(oper == '+') {
            x = max(x, min(w,h));
            y = max(y, max(w,h));
        } else {
            //cout << x << " " << y << " | " << h << " " << w << endl;
            cout << (((x <= h and y <= w) or (x <= w and y <= h))? "YES" : "NO") << endl;
        }
    }
    return 0;
}

