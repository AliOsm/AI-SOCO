//ITNOG
#include<bits/stdc++.h>
 
using namespace std;
 
 
#define int long long
#define rep(i, s, e) for(int i = s; i < e; i ++)
typedef double ld;

const int maxN = 100*1000 + 5;
const int mod = 1000*1000*1000+7;
const int maxL = 20;
typedef long long ll;
#define X first
#define Y second
int par[maxN];
int get_par(int v) { return (par[v] == -1 ? v : par[v] = get_par(par[v])); }
bool merge(int v, int u)
{
    v = get_par(v); u = get_par(u);
    if(v == u) return false;
    par[v] = u; return true;
}

vector<pair<int,int> > a[maxN];
int lca[maxN][maxL], dd[maxN][maxL], h[maxN];

void make_lca(int v, int par, int w)
{
    lca[v][0] = par; dd[v][0] = w;
    rep(i,1,maxL)
    {
	  lca[v][i] = lca[lca[v][i-1]][i-1];
	  dd[v][i] = max(dd[v][i-1], dd[lca[v][i-1]][i-1]);
    }
}

void dfs(int v, int par = 0, int w = 0)
{
    make_lca(v,par,w); h[v] = h[par]+1;
    for(auto u : a[v]) 
	  if(u.X - par)
		dfs(u.first,v,u.second);
}

int get_par(int v, int k)
{
    rep(i,0,maxL) if(k >> i & 1) v = lca[v][i];
    return v;
}

int LCA(int v, int u)
{
    if(h[v] < h[u]) swap(v,u);
    v = get_par(v,h[v]-h[u]);
    if(v==u) return v;
    for(int i = maxL-1; i >= 0; i --) 
	  if(lca[v][i] != lca[u][i]) v=lca[v][i], u=lca[u][i];
    return lca[v][0];
}

int get_ans(int v, int k)
{
    int ans = 0;
    rep(i,0,maxL) if(k >> i & 1) ans = max(ans, dd[v][i]), v = lca[v][i];
    return ans;
}

main()
{
    memset(par,-1,sizeof par);
    ios::sync_with_stdio(0); cin.tie(0);
    int n,m; cin >> n >> m;
    vector<pair<int,pair<int,int> > > ed, ms;
    rep(i,0,m)
    {
	  int v, u, w; cin >> v >> u >> w;
	  ed.push_back({w,{v,u}});
    }
    sort(ed.begin(), ed.end());
    
    int sum = 0;
    rep(i,0,m)
    {
	  int v = ed[i].Y.X, u = ed[i].Y.Y, w = ed[i].X;
	  if(merge(v,u)) { ms.push_back(ed[i]); sum += w;}
    }

    int q; cin >> q;
    if(ms.size() < n-2)
    {
	  rep(i,0,q) cout << "-1\n"; return 0; 
    }
    
    if(ms.size() == n-2)
    {
	  rep(i,0,q)
	  {
		int v, u; cin >> v >> u; 
		if(get_par(v) == get_par(u)) cout << "-1\n";
		else cout << sum << '\n';
	  }
	  return 0;
    }

    rep(i,0,n-1) 
    {
	  int v = ms[i].Y.X, u = ms[i].Y.Y, w = ms[i].X;
	  a[v].push_back({u,w});
	  a[u].push_back({v,w});
    }

    dfs(1);
    rep(i,0,q)
    {
	  int v, u; cin >> v >> u;
	  int par = LCA(v,u);
	  int tmp1 = get_ans(v,h[v]-h[par]);
	  int tmp2 = get_ans(u,h[u]-h[par]);
	  cout << sum - max(tmp1, tmp2) << '\n';
    }
    

    return 0;
}
