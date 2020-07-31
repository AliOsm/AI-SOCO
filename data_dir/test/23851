#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define REP(i,n) for(int i=0;i<n;++i)
#define REP1(i,n) for(int i=1;i<=n;++i)
#define SZ(i) int(i.size())
#define eb emplace_back
#define ALL(i) i.begin(),i.end()
#define X first
#define Y second
#ifdef tmd
#define IOS()
#define debug(...) fprintf(stderr,"#%d: %s = ",__LINE__,#__VA_ARGS__),_do(__VA_ARGS__);
template<typename T> void _do(T &&x){cerr<<x<<endl;}
template<typename T, typename ...S> void _do(T &&x, S &&...y){cerr<<x<<", ";_do(y...);}
template<typename It> ostream& _printRng(ostream &os,It bg,It ed)
{
    os<<"{";
    for(It it=bg;it!=ed;it++) {
        os<<(it==bg?"":",")<<*it;
    }
    os<<"}";
    return os;
}
template<typename T> ostream &operator << (ostream &os,vector<T> &v){return _printRng(os,v.begin(), v.end());}
template<typename T> void pary(T bg, T ed){_printRng(cerr,bg,ed);cerr<<endl;}
#else
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define debug(...)
#define pary(...)
#endif

const int MAXN = 200005;
const ll MOD = 1000000007;

int n, wh[MAXN], dp[MAXN], wsz[MAXN], bsz[MAXN];
vector<int> edge[MAXN];

void build_sz (int nd, int par) {
    wsz[nd] = wh[nd];
    bsz[nd] = 1 - wh[nd];

    for (auto v : edge[nd]) {
        if ( v != par ) {
            build_sz(v, nd);
            wsz[nd] += wsz[v];
            bsz[nd] += bsz[v];
        }
    }
}

void build_dp (int nd, int par) {
    dp[nd] = bsz[nd] - wsz[nd];
    int res = 0;
    for (int v : edge[nd]) {
        if (v != par) {
            build_dp(v, nd);
            res += dp[v];
        }
    }
    dp[nd] = max({dp[nd], res, 0});
}

int ans[MAXN];
void solve (int nd, int par, int tp) {

    ans[nd] = wsz[1] - bsz[1] + tp;

    int res = 0;
    for (auto v : edge[nd]) {
        if (v == par) {
            continue;
        }
        res += dp[v];
    }

    ans[nd] += res;
    for (auto v : edge[nd]) {
        if (v != par) {
            int cur = bsz[1] - wsz[1] - bsz[v] + wsz[v];
            solve(v, nd, max(cur, tp+res-dp[v]));
        }
    }
}
/*********************GoodLuck***********************/
int main () {
    IOS();

    cin >> n;
    for (int i=1; i<=n; i++) {
        cin >> wh[i];
    }

    for (int i=0; i<n-1; i++) {
        int u, v;
        cin >> u >> v;
        edge[u].emplace_back(v);
        edge[v].emplace_back(u);
    }
    build_sz(1, 1);
    build_dp(1, 1);
    solve(1, 1, 0);

    pary(dp+1, dp+1+n);
    for (int i=1; i<=n; i++) {
        cout << ans[i] << " \n"[i==n];
    }

}

