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

/* Good Luck && Have Fun ! */

const int maxn = 1.12e5;
int a[maxn];
struct node
{
	ll s; int mx;
} t[maxn<<2];
inline int LC(int o) {return o + o + 1;}
inline int RC(int o) {return LC(o) + 1;}
inline void pull(int o)
{
	t[o].s = t[LC(o)].s + t[RC(o)].s;
	t[o].mx = max(t[LC(o)].mx, t[RC(o)].mx);
}
void build(int o,int l,int r)
{
	if (r - l == 1) {
		t[o].s = t[o].mx = a[l];
		return;
	}
	int m = l + ((r - l) >> 1);
	build(LC(o),l,m);
	build(RC(o),m,r);
	pull(o);
}
ll qry(int o,int l,int r,int i,int j)
{
	if (r <= i || j <= l)
		return 0;
	if (i <= l && r <= j)
		return t[o].s;
	int m = l + ((r - l) >> 1);
	return qry(LC(o),l,m,i,j) + qry(RC(o),m,r,i,j);
}
void mod(int o,int l,int r,int i,int j,int x)
{
	if (r <= i || j <= l || t[o].mx < x)
		return;
	if (r - l == 1) {
		t[o].mx = (t[o].s %= x);
		return;
	}
	int m = l + ((r - l) >> 1);
	mod(LC(o),l,m,i,j,x);
   	mod(RC(o),m,r,i,j,x);
	pull(o);
}
void chg(int o,int l,int r,int i,int x)
{
	if (r - l == 1) {
		t[o].mx = t[o].s = x;
		return;
	}
	int m = l + ((r - l) >> 1);
	if (i < m)
		chg(LC(o),l,m,i,x);
	else
		chg(RC(o),m,r,i,x);
	pull(o);
}
int main()
{
	int n,m;
	RD(n,m);
	RP(i,n)
		RD(a[i]);
	build(0,0,n);
	while (m--) {
		int p,l,r,x;
		RD(p);
		switch (p) {
			case 1:
				RD(l,r);
				printf("%lld\n", qry(0,0,n,l-1,r));
				break;
			case 2:
				RD(l,r,x);
				mod(0,0,n,l-1,r,x);
				break;
			case 3:
				RD(l,x);
				chg(0,0,n,l-1,x);
				break;
		}
	}
}
