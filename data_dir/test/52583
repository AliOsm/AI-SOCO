#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll maxn = 2e5+5;
ll n, m;
ll a[maxn];
struct Spec
{
    ll u, v;
    ll w;
};

//dsu
ll parent[maxn]; //memset to -1
ll Find(ll x) {
    return parent[x] < 0 ? x : parent[x] = Find(parent[x]);
}

void Union(ll x, ll y) {
    x = Find(x);
    y = Find(y);
    if (x == y) return;
    if (parent[x] > parent[y]) swap(x,y);
    parent[x] += parent[y];
    parent[y] = x;
}

int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n >> m;
    for (ll i = 0; i <= n; i++) parent[i] = -1;
    for (ll i = 1; i <= n; i++) cin >> a[i];
    vector<Spec> specs;
    for (ll i = 0; i < m; i++) {
        ll x, y, w; cin >> x >> y >> w;
        Spec s = {x,y,w};
        specs.push_back(s);
    }
    vector<pair<ll,ll>> ps;
    for (ll i = 1; i <= n; i++) {
        ps.push_back({a[i],i});
    }
    sort(ps.begin(),ps.end(),[](auto& a, auto& b) {
            return a.first < b.first;
            });
    ll mincost = ps[0].first;
    ll root = ps[0].second;
    for (int i = 1; i < n; i++) {
        Spec s = {ps[i].second,root,ps[i].first+mincost};
        specs.push_back(s);
    }
    sort(specs.begin(),specs.end(),[](auto& a, auto& b) {
            return a.w < b.w;
            });
    ll ans = 0;
    for (Spec s: specs) {
        if (Find(s.u) != Find(s.v)) {
            Union(s.u,s.v);
            //cout << s.w << '\n';
            ans += s.w;
        }
    }
    cout << ans << '\n';

    return 0;
}
