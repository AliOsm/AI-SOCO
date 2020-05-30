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

vector<ll> square;
ll x;

bool check(int pos) {
    ll ok = sqrt(square[pos]);
    ll tot = square[pos];

    for(ll m = 1; m <= ok; m++) {
        ll tmp = (ok/m) * (ok/m);
        if(tot - tmp == x) {
            cout << ok << " " << m << endl;
            return true;
        }
        if(tot - tmp > x) return false;
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    for(ll i = 1; i*i <= 1e12; i++) square.pb(i*i);

    int q; cin >> q;

    while(q--) {
        cin >> x;
        int pos = lower_bound(square.begin(), square.end(), x) - square.begin();
        bool flag = 1;
        for(int i = pos; i < pos+10000 and i < square.size(); i++) {
            if(check(i)) { flag = 0; break; }
        }
        if(flag) cout << -1 << endl;
    }

    return 0;
}

