#include <bits/stdc++.h>
using namespace std;
// daily life
#define REP(i,s,e) for (int i = (s), __e = (e); i < __e; ++i)
#define RP(i,n) REP(i,0,n)
#define PER(i,s,e) for (int i = (s) - 1, __e = (e); i >= __e; --i)
#define PR(i,n) PER(i,n,0)
#define DO(n) REP(__i,0,n)
template<typename T>
void cmax(T & a, T b) {a = max(a, b);}
template<typename T>
void cmin(T & a, T b) {a = min(a, b);}

// data type
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define F first
#define S second

// STL container
typedef vector<int> vi;
typedef vector<ll> vll;
#define SZ(a) ((int)a.size())
#define ALL(a) a.begin(), a.end()
#define CLR(a) a.clear()
#define DB(a) a.pop_back()
#define DF(a) a.pop_front()
#define PB push_back
#define EB emplace_back

// input
bool RD(void) {return true;}
bool RD(int & a) {return scanf("%d", &a) == 1;}
bool RD(ll & a) {return scanf("%lld", &a) == 1;}
bool RD(double & a) {return scanf("%lf", &a) == 1;}
bool RD(char & a) {return scanf(" %c", &a) == 1;}
bool RD(char * a) {return scanf("%s", a) == 1;}
template<typename T, typename ... TT>
bool RD(T & a, TT & ...  b) {return RD(a) && RD(b...);}

/* Good Luck && Have Fun ! */

const int maxn = 2.28e5;
int n, m;
int a[maxn], d[maxn];
vi g[maxn];
int cnt;
pii rg[maxn];
int B[maxn];
void dfs(int dep, int p, int u)
{
	d[u] = dep;
	rg[u].F = ++cnt;
	for (auto v : g[u])
		if (v != p) 
			dfs(dep + 1, u, v);
	rg[u].S = cnt + 1;
}
void add(int i, int v)
{
	for ( ; i <= n; i += i & -i)
		B[i] += v;
}
int qry(int i)
{
	int ret = 0;
	for ( ; i; i ^= i & -i)
		ret += B[i];
	return ret;
}
int main()
{
	RD(n, m);
	REP(i,1,n+1)
		RD(a[i]);
	DO(n-1) {
		int u, v;
		RD(u,v);
		g[u].PB(v);
		g[v].PB(u);
	}
	dfs(0,0,1);
	while (m--) {
		int t, x, v;
		RD(t, x);
		if (t == 1) {
			RD(v);
			if (d[x] & 1)
				v = -v;
			add(rg[x].F, v);
			add(rg[x].S, -v);
		} else {
			printf("%d\n", a[x] + ((d[x]&1) ? -1 : 1) * qry(rg[x].F));
		}
	}
}
