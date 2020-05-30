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
typedef pair<int,int> ii;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int T = 1e5 + 5;
const int N = 5*T*log2(T);

int p[T], tin[T], tout[T], niv[T], volta[T];
vector<int> g[T];
vector<int> h[T];
int n,r,nodes,t, maxNiv;

int seg[N], root[T], L[N], R[N];

void dfs(int u, int pai) {
    tin[u] = ++t;
    volta[t] = u;
    h[niv[u]].pb(u);

    maxNiv = max(maxNiv,niv[u]);

    for(int v : g[u]) {
        if(v != pai) {
            niv[v] = niv[u]+1;
            dfs(v,u);
        }
    }
    tout[u] = t;

}

int build(int i, int j) {
    int at = ++nodes;

    if(i == j) {
        seg[at] = INF;
    } else {
        int mid = (i+j) >> 1;
        L[at] = build(i,mid);
        R[at] = build(mid+1,j);
        seg[at] = INF;
    }

    return at;
}

int update(int node, int i, int j, int pos) {
    if(i > pos or j < pos) return node;
    int at = ++nodes;

    if(i == pos and j == pos) {
        seg[at] = p[volta[pos]];
    } else {
        int mid = (i+j) >> 1;
        L[at] = update(L[node],i,mid,pos);
        R[at] = update(R[node],mid+1,j,pos);
        seg[at] = min(seg[L[at]],seg[R[at]]);
    }

    return at;
}

int query(int node, int i, int j, int a, int b) {
    if(i > b or j < a) return INF;
    if(i >= a and j <= b) return seg[node];
    int mid = (i+j) >> 1;
    return min(query(L[node],i,mid,a,b),query(R[node],mid+1,j,a,b));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> r;
    for(int i = 1; i <= n; i++) cin >> p[i];

    for(int i = 0; i < n-1; i++) {
        int a,b; cin >> a >> b;
        g[a].pb(b);
        g[b].pb(a);
    }

    niv[r] = 1;
    dfs(r,r);
    root[0] = build(1,t);

    for(int i = 1; i <= maxNiv; i++) {
        root[i] = root[i-1];
        for(int v : h[i]) {
            root[i] = update(root[i],1,t,tin[v]);
        }
    }

    int q; cin >> q;
    int last = 0;

    while(q--) {
        int x,k; cin >> x >> k;
        x = (x + last)%n + 1;
        k = (k + last)%n;
        int ver = min(niv[x]+k,maxNiv);
        last = query(root[ver], 1, t, tin[x],tout[x]);
        cout << last << endl;
    }

    return 0;
}

