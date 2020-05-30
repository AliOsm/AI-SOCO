#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
#define W first
#define V second
#define eb emplace_back
#define pb push_back
const int maxn = 2.28e5;
const int maxd = __lg(maxn) + 1;
struct edge
{
	int u, v, w, i;
	edge() {}
	edge(int a, int b, int c) : u(a), v(b), w(c) {}
	bool operator < (const edge & x) const
	{
		return w < x.w;
	}
};
edge e[maxn];
ll ans[maxn];
int p[maxn];
vector<pii> g[maxn];
int ac[maxd][maxn];
int mxw[maxd][maxn];
/* ac[i][u]: 2^i th ancestor of u
 * mxw[i][u]: heaviest weight from u to ac[i][u]
 */
int dep[maxn];
ll mstw;
int find(int x) {return p[x] == x ? x : p[x] = find(p[x]);}
void join(edge & a)
{
	p[find(a.u)] = find(a.v);
	g[a.u].eb(a.w, a.v);
	g[a.v].eb(a.w, a.u);
	mstw += a.w;
	a.w = 0;
}
void dfs(int d, int pa, int u, int w)
{
	dep[u] = d;
	int ep =__lg(d);
	ac[0][u] = pa;
	mxw[0][u] = w;
	for (int i = 1; i <= ep; ++i)
		ac[i][u] = ac[i-1][ac[i-1][u]];
	for (int i = 1; i <= ep; ++i)
		mxw[i][u] = max(mxw[i-1][u], mxw[i-1][ac[i-1][u]]);
	for (auto x : g[u])
		if (x.V != pa)
			dfs(d+1, u, x.V, x.W);
}
int main()
{
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; ++i) {
		scanf("%d%d%d", &e[i].u, &e[i].v, &e[i].w);
		e[i].i = i;
	}
	sort(e, e + m);
	for (int i = 1; i <= n; ++i)
		p[i] = i;
	for (int i = 0; i < m; ++i)
		if (find(e[i].u) != find(e[i].v))
			join(e[i]);
	dfs(0, 0, 1, 0);
	for (int i = 0; i < m; ++i) {
		if (!e[i].w) {
			ans[e[i].i] = mstw;
			continue;
		} 
		int u = e[i].u, v = e[i].v;
		if (dep[u] < dep[v])
			swap(u, v);
		int mx = 0;
		while (dep[u] > dep[v]) {
			int k = __lg(dep[u] - dep[v]);
			mx = max(mx, mxw[k][u]);
			u = ac[k][u];
		}
		while (u != v) {
			int k = __lg(dep[u]);
			while (k && ac[k][u] == ac[k][v])
				--k;
			mx = max(mx, max(mxw[k][u], mxw[k][v]));
			u = ac[k][u];
			v = ac[k][v];
		}
		ans[e[i].i] = mstw - mx + e[i].w;
	}
	for (int i = 0; i < m; ++i)
		printf("%lld\n", ans[i]);
}
