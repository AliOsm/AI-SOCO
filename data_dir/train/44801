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
#define endl '\n'
#define debug(...)
#endif

const int MAXN = 100005;
const ll MOD = 1000000007;
const int MAXC = 31;
struct Solve {
    ll xLim, yLim;
    ll dp[MAXC][2][2]; // digit, x-bounded, y-bounded
    Solve(ll X, ll Y) : xLim(X), yLim(Y) {
        memset(dp, -1, sizeof(dp));
    }

    ll solve (ll d, bool xB, bool yB) {
        if (d == -1) {
            return 1;
        } else if (dp[d][xB][yB] != -1) {
            return dp[d][xB][yB];
        }
        ll &cdp = dp[d][xB][yB];
        cdp = 0;

        ll xD = (xLim>>d) & 1, yD = (yLim>>d) & 1;
        REP (x, 2) {
            REP (y, 2) {
                if ((x && y) || (xB && (x > xD)) || (yB && (y > yD))) {
                    continue;
                }
                cdp += solve(d-1, xB&&(x == xD), yB&&(y == yD));
            }
        }

        return cdp;
    }

    ll get () {
        if (xLim < 0 || yLim < 0) {
            return 0;
        } else {
            return solve(MAXC-1, true, true);
        }
    }
};
/*********************GoodLuck***********************/
int main () {
    IOS();
    int t;
    cin >> t;
    while (t--) {
        ll l, r;
        cin >> l >> r;
        l--;
        Solve RR(r, r), LR(l, r), LL(l, l);
        cout << RR.get() - LR.get() * 2 + LL.get() << endl;
    }
}
