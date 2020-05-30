#include <bits/stdc++.h>
using namespace std;
// nichijou
#define REP(i,a,b) for (int i(a), _B(b); i < _B; ++i)
#define RP(i,n) REP(i,0,n)
#define PER(i,a,b) for(int i((a)-1), _B(b); i >= _B; --i)
#define PR(i,n) PER(i,n,0)
#define REP1(i,a,b) REP(i,a,(b)+1)
#define RP1(i,n) REP1(i,1,n)
#define PER1(i,a,b) PER(i,(a)+1,b)
#define PR1(i,n) PER1(i,n,1)
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
#define BK(a) (a.back())
#define FT(a) (a.front())
#define DB(a) a.pop_back()
#define DF(a) a.pop_front()
#define PB push_back
#define EB emplace_back

/* I gave you my heart and then you turned around. */
void _BG(const char * s) {}
template<typename T, typename ... TT>
void _BG(const char * s,T a, TT...b)
{
	for (int c = 0; *s && (c || *s != ','); ++s) {
		cerr<<*s;
		switch (*s) {
		case '(':
		case '[':
		case '{':
			++c;
			break;
		case ')':
		case ']':
		case '}':
			--c;
			break;
		}
	}
	cerr<<" = "<<a;
	if (*s) {
		cerr<<", ";
		_BG(++s,b...);
	} else
		cerr<<endl;
}
#define BG(...) do { \
	cerr << __PRETTY_FUNCTION__ << ':' << __LINE__ << ": "; \
	_BG(#__VA_ARGS__,__VA_ARGS__); \
} while(0)

/* Reading input is now 20% cooler! */
bool RD(void) {return true;}
bool RD(char & a) {return scanf(" %c", &a) == 1;}
bool RD(char * a) {return scanf("%s", a) == 1;}
bool RD(double & a) {return scanf("%lf", &a) == 1;}
bool RD(int & a) {return scanf("%d", &a) == 1;}
bool RD(ll & a) {return scanf("%lld", &a) == 1;}

template<typename T, typename ... TT>
bool RD(T & a, TT & ...  b) {return RD(a) && RD(b...);}

/* Do princesses dream of magic sheep? */
#define RI(a) int a; RD(a)
#define RII(a,b) RI(a); RI(b)
#define RIII(a,b,c) RI(a); RII(b,c)
#define RIIII(a,b,c,d) RI(a); RIII(b,c,d)

/* For it's time for you to fulfill your output. */
void PT(const char a) {putchar(a);}
void PT(const char * a) {fputs(a, stdout);}
void PT(char * a) {fputs(a, stdout);}
void PT(const double a) {printf("%.16f", a);}
void PT(const int a) {printf("%d", a);}
void PT(const ll a) {printf("%lld", a);}

/* The line will last forever! */
template<char sep = ' ',char end = '\n'>
void PL(void) {if (end) PT(end);}
template<char sep = ' ',char end = '\n',typename T, typename ... TT>
void PL(const T a, const TT ...  b) {PT(a); if (sizeof...(b) && sep) PT(sep); PL<sep,end>(b...);}

/* Good Luck && Have Fun ! */
const int N = 1e6 + 87;
const int D = __lg(N) + 1;
vi g[N];
int pa[N], de[N], sz[N], mi[D][N], cv[N], a[N][2];
bool bl[N];
void getsz(int p,int u)
{
	sz[u] = 1;
	for (int v : g[u])
		if (v != p) {
			getsz(u,v);
			sz[u] += sz[v];
		}
}
int fct(int p,int u,int n)
{
	for (int v : g[u]) if (v != p) 
		if (sz[v] > n/2)
			return fct(u,v,n);
	return u;
}
void dfs(int p,int u,int d)
{
	mi[d][u] = min(u, mi[d][p]);
	for (int v : g[u]) if (v != p)
		dfs(u,v,d);
}
void bld(int p,int u,int d)
{
	u = fct(0,u,sz[u]);
	pa[u] = p;
	de[u] = d;
	mi[d][u] = u;
	for (int v : g[u]) {
		for (int & k : g[v])
			if (k == u) {
				k = g[v].back();
				g[v].pop_back();
				break;
			}
		dfs(u,v,d);
		if (sz[v] > sz[u])
			getsz(0,v);
	}
	for (int v : g[u])
		bld(u,v,d+1);
}
void upd(int u)
{
	bl[u] = 1;
	for (int v = pa[u], k = u, d = de[u] - 1; v; k = v, v = pa[v], --d) {
		int t = mi[d][u];
		if (t < cv[k]) {
			cv[k] = t;
			int & x = a[v][0], & y = a[v][1];
			if (k == y) {
				if (cv[k] < cv[x])
					swap(x,y);
			} else if (k != x) {
				if (cv[k] < cv[x]) {
					y = x;
					x = k;
				} else if (cv[k] < cv[y]) {
					y = k;
				}
			}
		}
	}
}
int qry(int u)
{
	int ans = bl[u] ? u : N;
	if (a[u][0])
		cmin(ans, cv[a[u][0]]);
	for (int v = pa[u], k = u, d = de[u] - 1; v; k = v, v = pa[v], --d) {
		if (bl[v])
			cmin(ans, mi[d][u]);
		for (int i : a[v])
			if (i != k) {
				if (i)
					cmin(ans, min(mi[d][u], cv[i]));
				break;
			}
	}
	return ans;
}
int main()
{
	RII(n,q);
	DO(n-1) {
		RII(u,v);
		g[u].PB(v);
		g[v].PB(u);
	}
	getsz(0,1);
	bld(0,1,0);
	fill_n(cv,n+1,N);
	int ans = 0;
	DO(q) {
		RII(t,z);
		int x = (z + ans) % n + 1;
		if (t == 1) {
			upd(x);
		} else {
			PL(ans = qry(x));
		}
	}
}
