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
const int T = 1e5 + 20;
const int LOG = 20;
int t;
int n, m;
int pai[T];
int nivel[T];
int in[T];
int out[T];
int ancestral[T][LOG];
vector<int> g[T];
vector<int> depth[T];

int kth(int u, int niv) {
    niv = nivel[u] - niv;
    for(int i = LOG -1; i >= 0; i--)
        if(nivel[u] - (1<<i) >= niv) 
            u = ancestral[u][i];
    return u;
}

void query() {
    cin >> m;
    int u, niv;
    for(int i = 0; i < m; i++) {
        cin >> u >> niv;
        int anc = kth(u,niv);
        if(anc < 0) cout << 0 << " "; 
        else {
            int l = upper_bound(depth[nivel[u]].begin(), depth[nivel[u]].end(), in[anc]) - depth[nivel[u]].begin();
            int r = upper_bound(depth[nivel[u]].begin(), depth[nivel[u]].end(), out[anc]) - depth[nivel[u]].begin();
            cout << max(0, r-l-1) << " ";
        }
    }
    cout << endl;
}

void dfs(int u) {
    in[u] = ++t;
    depth[nivel[u]].pb(in[u]);
    for(int i = 0; i < g[u].size(); i++) {
        int v = g[u][i];
        nivel[v] = nivel[u] + 1;
        dfs(v);
    }
    out[u] = ++t;
}

void build() {
    memset(nivel, -1, sizeof nivel);
    memset(ancestral, -1, sizeof ancestral);
    for(int i = 1; i <= n; i++) 
        if(nivel[i] == -1) { nivel[i] = 0; dfs(i); }
    for(int i = 1; i <= n; i++) ancestral[i][0] = pai[i];
    for(int j = 1; j < LOG; j++)
        for(int i = 1; i <= n; i++) 
            ancestral[i][j] = ancestral[ancestral[i][j-1]][j-1];
}

void read() {
    cin >> n;
    memset(pai, -1, sizeof pai);
    for(int i = 1; i <= n; i++) {
        cin >> pai[i];
        g[pai[i]].pb(i);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    read();
    build();
    query();
    return 0;
}
