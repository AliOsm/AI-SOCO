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
const ll MOD = 1e9+7;

ll query(int pos, const vector<ll> &bit) {
    ll ans = 0;
    for(; pos;pos-=pos&(-pos)) ans = (ans+bit[pos])%MOD;
    return ans;
}

void update(int pos, ll val, vector<ll> &bit) {
    for(;pos<bit.size();pos+=pos&(-pos)) bit[pos] = (bit[pos]+val)%MOD;
}

void updateBag(vii &bag, vector<ll> &bit) {
    while(bag.size()) {
        ll val;
        int s;
        tie(val,s) = bag.back();
        bag.pop_back();
        update(s,val,bit);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int n,m;
    vii v, bag;
    map<int,int> id;

    cin >> n >> m;

    for(int i = 0; i < m; i++) {
        int s,t;
        cin >> s >> t;
        v.eb(s,t);
        id[s] = id[t] = 1;
    }

    int ok = 0;
    for(auto x : id) id[x.fi] = ++ok;
    vector<ll> bit(ok+10);

    sort(v.begin(),v.end(), [&] (const ii &a, const ii &b) {
            if(a.se != b.se) return a.se > b.se;
            return a.fi < b.fi;
        });

    int last = -1;
    ll ans = 0;

    for(int i = 0; i < m; i++) {
        int s,t;
        tie(s,t) = v[i];
        if(t != last) updateBag(bag,bit);
        ll res = (query(id[t],bit)+(t==n))%MOD;
        bag.eb(res,id[s]);
        last = t;
        if(s == 0) ans = (ans+res)%MOD;
    }

    cout << ans << endl;

    return 0;
}

