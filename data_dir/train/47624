#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<n;i++)
#define REP1(i,n) for(int i=1;i<=n;i++)
#define SZ(i) int(i.size())
#ifdef tmd
#define IOS()
#define debug(...) fprintf(stderr,"%s - %d (%s) = ",__PRETTY_FUNCTION__,__LINE__,#__VA_ARGS__);_do(__VA_ARGS__);
template<typename T> void _do(T &&x){cerr<<x<<endl;}
template<typename T, typename ...S> void _do(T &&x, S &&...y){cerr<<x<<", ";_do(y...);}
#else
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0);
#define debug(...)
#endif

const int MAXN = 100005;
const ll MOD = 1000000007;

ll getArea(ll i, ll j, ll k) {
    ll ret = 0;
    cout << 1 << " " << i << " " << j << " " << k << endl;
    cin >> ret;
    return ret;
}

ll getSign(ll i, ll j, ll k) {
    ll ret = 0;
    cout << 2 << " " << i << " " << j << " " << k << endl;
    cin >> ret;
    return ret;
}

struct Point {
    ll hf, sg, area, id;
    bool operator < (const Point &oth) const {
        if (hf != oth.hf) {
            return hf < oth.hf;
        } else if (sg != oth.sg) {
            return sg < oth.sg;
        } else {
            if (sg > 0) {
                return area > oth.area;
            } else {
                return area < oth.area;
            }
        }
    }
} pts[1003];

void build (vector<ll> pid) {
    if (pid.empty()) {
        return;
    }

    ll mx = pid.front();
    for (auto p : pid) {
        pts[p].area = getArea(1, 2, p);
        if (pts[p].area > pts[mx].area) {
            mx = p;
        }
    }

    for (auto p : pid) {
        if (p != mx) {
            pts[p].sg = getSign(p, 1, mx);
        }
    }
}
/*********************GoodLuck***********************/
int main () {
    IOS();

    ll n;
    cin >> n;
    REP1 (i, n) {
        pts[i].id = i;
    }
    pts[1].hf = -1;
    pts[1].sg = -2;

    vector<ll> up, lw;
    for (ll i=3; i<=n; i++) {
        pts[i].hf = getSign(1, 2, i);
        if (pts[i].hf > 0) {
            up.emplace_back(i);
        } else {
            lw.emplace_back(i);
        }
    }

    build(up), build(lw);

    sort(pts+1, pts+n+1);
    assert(pts[1].id == 1);

    cout << 0;
    REP1 (i, n) {
        cout << " " << pts[i].id;
    }
    cout << endl;
}
