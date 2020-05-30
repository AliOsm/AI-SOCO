#include <bits/stdc++.h>
using namespace std;

#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int T = 5e3 + 3;
bool vis[T];
bool vout[T];
vector<ii> arestas;
vector<int> g[T];
int n,m,t,ans;
int r[T];

void dfs(int u) {
    vis[u] = 1;

    for(int x : g[u]) {
        int v = arestas[x].se;

        if(!vis[v]) dfs(v);
        else if(!vout[v]) r[x] = 1, ans = 2;
    }

    vout[u] = 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    int a,b;
    cin >> n >> m;

    for(int i = 0; i < m; i++) {
        cin >> a >> b;
        g[a].pb(arestas.size());
        arestas.eb(a,b);
    }

    ans = 1;
    for(int i = 1; i <= n; i++) if(!vis[i]) dfs(i);

    cout << ans << endl;
    for(int i = 0; i < m; i++) cout << r[i]+1 << " ";
    cout << endl;

    return 0;
}

