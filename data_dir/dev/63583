#include <bits/stdc++.h>
using namespace std;
// nichijou
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
#define BK(a) (a.back())
#define FT(a) (a.front())
#define DB(a) a.pop_back()
#define DF(a) a.pop_front()
#define PB push_back
#define EB emplace_back

/* reading input is now 20% cooler */
bool RD(void) {return true;}
bool RD(int & a) {return scanf("%d", &a) == 1;}
bool RD(ll & a) {return scanf("%lld", &a) == 1;}
bool RD(double & a) {return scanf("%lf", &a) == 1;}
bool RD(char & a) {return scanf(" %c", &a) == 1;}
bool RD(char * a) {return scanf("%s", a) == 1;}
template<typename T, typename ... TT>
bool RD(T & a, TT & ...  b) {return RD(a) && RD(b...);}

/* For it's time for you to fulfill your output */
void PT(const int a) {printf("%d", a);}
void PT(const ll a) {printf("%lld", a);}
void PT(const double a) {printf("%.16f", a);}
void PT(const char a) {putchar(a);}
void PT(const char * a) {fputs(a, stdout);}

/* The line will last forever! */
void PL(void) {PT('\n');}
template<typename T, typename ... TT>
void PL(const T a, const TT ...  b) {PT(a); if (sizeof...(b)) PT(' '); PL(b...);}

/* Good Luck && Have Fun ! */
map<string,int> id;
const int N = 1e5 + 87;
char s[26], d[26];
int p[N], h[N];
int find(int x) {return x == p[x] ? x : p[x] = find(p[x]);}
int meld(int a, int b)
{
	if (a == -1 || b == -1)
		return a == -1 ? b : a;
	a = find(a);
	b = find(b);
	p[a] = b;
	return b;
}
int main()
{
	int n,m,q;
	RD(n,m,q);
	RP(i,n) {p[i] = i; h[i] = -1;}
	RP(i,n) {
		RD(s);
		id[s] = i;
	}
	while (m--) {
		int t;
		RD(t,s,d);
		int u = find(id[s]), v = find(id[d]);
		if (t == 1) {
			if (h[u] != -1 && find(h[u]) == v) {
				PL("NO");
			} else {
				PL("YES");
				if (u == v)
					continue;
				int x = meld(u, v);
				int y = meld(h[u], h[v]);
				h[x] = y;
				if (y != -1)
					h[y] = x;
			}
		} else {
			if (u == v) { 
				PL("NO");
			} else {
				PL("YES");
				if (h[u] != -1 && find(h[u]) == v)
					continue;
				int x = meld(u, h[v]);
				int y = meld(v, h[u]);
				h[x] = y;
				h[y] = x;
			}
		}
	}
	while (q--) {
		RD(s,d);
		int u = find(id[s]), v = find(id[d]);
		PL(u == v ? 1 : (h[v] != -1 && u == find(h[v]) ? 2 : 3));
	}
}
