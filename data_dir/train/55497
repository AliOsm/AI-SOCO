#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;

const int T = 1e5 + 2;

unordered_map<ll,ll> id;
unordered_map<ll,ll> qtd;
unordered_set<ll> bag;
vector<ll> g[T];
bool vis[T];
int in[T];
int cont;
ll n,k;
ll lim = 1e9 + 2;

ii dfs(int at, bool cor) {
    vis[at] = 1;
    ii ok = mk(0,0);

    if(cor == 0) ok.fi = qtd[at];
    else ok.se = qtd[at];

    for(auto v : g[at]) {
        if(!vis[v]) {
            ii tmp = dfs(v,!cor);
            ok.fi += tmp.fi;
            ok.se += tmp.se;
        }
    }

    return ok;
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> k;
    int x;

    for(int i = 0; i < n; i++) {
        cin >> x;
        if(bag.count(x)) qtd[id[x]]++; 
        else {
            bag.insert(x);
            id[x] = cont++;
            qtd[id[x]] = 1;
        }
    }

    if(k == 1) { cout << bag.size() << endl; return 0; }

    for(ll v : bag) {
        if(lim/k < v) continue;
        if(bag.count(v*k)) {
            g[id[v]].pb(id[v*k]);
            in[id[v*k]]++;
        }
    }

    ll ans = 0;

    for(ll v : bag) {
        if(!vis[id[v]] and !in[id[v]]) {
            ii ok = dfs(id[v],0);
            ans += max(ok.fi, ok.se);
        }
    }

    cout << ans << endl;

    return 0;
}

