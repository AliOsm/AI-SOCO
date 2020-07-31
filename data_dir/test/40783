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

const int MAXN = 5003;
const ll MOD = 998244353;

int n, a[MAXN];
ll dp[MAXN][MAXN];
ll inv[MAXN];
int cnt[MAXN];

ll mpow (ll bs, ll ep) {
    ll res = 1;
    while (ep) {
        if (ep&1) {
            res = res * bs % MOD;
        }
        bs = bs * bs % MOD;
        ep >>= 1;
    }
    return res;
}

/*********************GoodLuck***********************/
int main () {
    IOS();

    for (int i=1; i<MAXN; i++) {
        inv[i] = mpow(i, MOD-2);
    }

    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> a[i];
        cnt[a[i]]++;
    }
    sort(a, a+n);

    for (int i=n; i>0; i--) {
        int pcnt = 0;
        ll pdp = 0;
        for (int j=n; j>=0; j--) {
            int R = n-i+1;

            dp[i][j] = pdp * inv[R] % MOD;

            if (cnt[j]) {
                dp[i][j] += (cnt[j]-1) * inv[R] % MOD;
            }

            dp[i][j] %= MOD;

            pcnt += cnt[j];
            pdp += cnt[j] * dp[i+1][j];

            pcnt %= MOD;
            pdp %= MOD;
        }
        pary(dp[i], dp[i]+n+1);
    }

    cout << dp[1][0] << endl;


}

