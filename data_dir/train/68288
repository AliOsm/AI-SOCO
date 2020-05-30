#include <bits/stdc++.h>
using namespace std;

#define fr(i,n) _back
#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int T = 1e5;
const ll MOD = 1e9+7;

bitset<T> crivo;
vector<ll> primes;
vector<ll> dvs;
vector<ii> ans;
ll lim = 1e18;
ll n,z;

void init() {
    for(int i = 2; i < T; i++) {
        if(!crivo[i]) {
            primes.pb(i);
            for(int j = i+i; j < T; j += i) crivo[j] = 1;
        }
    }
}

void decop(ll x) {
    for(int i = 0; i < primes.size() and primes[i] * primes[i] <= x; i++) {
        if(x % primes[i] == 0) {
            dvs.pb(primes[i]);
            while(x % primes[i] == 0) x /= primes[i];
        }
    }
    if(x > 1) dvs.pb(x);
}

ll ele(ll base, ll e) {
    ll ans = 1;
    base %= MOD;

    while(e) {
        if(e&1) ans = (ans * base) % MOD;
        base = (base * base) % MOD;
        e >>= 1;
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);

    init();
    cin >> z >> n;
    decop(z);

    for(int i = 0; i < dvs.size(); i++) {
        ll ok = dvs[i];
        int pas = 0;
        while(1) {
            ll t = n/ok;
            if(t) {
                if(pas > 0) ans.back().se -= t;
                ans.eb(ok,t);
                pas++;
            } else break;

            if(ok <= lim/dvs[i]) ok *= dvs[i];
            else break;
        }
    }

    ll r = 1;
    for(int i = 0; i < ans.size(); i++) {
        r = (r * ele(ans[i].fi,ans[i].se)) % MOD;
        //cout << ans[i].fi << " " << ans[i].se << endl;
    }
    cout << r << endl;

    return 0;
}
