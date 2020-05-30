#include <bits/stdc++.h>
using namespace std;
// nichijou
#define REP(i,a,b) for (int i = (a), __e = (b); i < __e; ++i)
#define RP(i,n) REP(i,0,n)
#define PER(i,s,e) for (int i = (s) - 1, __e = (e); i >= __e; --i)
#define PR(i,n) PER(i,n,0)
#define REP1(i,a,b) for (int i = (a), __e = (b); i <= __e; ++i)
#define RP1(i,n) REP1(i,1,n)
#define PER1(i,s,e) for (int i = (s), __e = (e); i >= __e; --i)
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

/* Reading input is now 20% cooler! */
bool RD(void) {return true;}
bool RD(int & a) {return scanf("%d", &a) == 1;}
bool RD(ll & a) {return scanf("%lld", &a) == 1;}
bool RD(double & a) {return scanf("%lf", &a) == 1;}
bool RD(char & a) {return scanf(" %c", &a) == 1;}
bool RD(char * a) {return scanf("%s", a) == 1;}
template<typename T, typename ... TT>
bool RD(T & a, TT & ...  b) {return RD(a) && RD(b...);}

/* Do princesses dream of magic sheep? */
#define DRI(a) int a; RD(a)
#define DRII(a,b) DRI(a); DRI(b)
#define DRIII(a,b,c) DRI(a); DRII(b,c)
#define DRIIII(a,b,c,d) DRI(a); DRIII(b,c,d)

/* For it's time for you to fulfill your output. */
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
const int N = 1.12e5;
const ll inf = 3e18;
ll x[N],y[N];
int p[N],tmp[N];
inline ll sqr(ll x) {return x * x;}
inline ll dis(int i,int j) {return sqr(x[i] - x[j]) + sqr(y[i] - y[j]);}
ll DC(int l, int r)
{
	ll ret = inf;
	if (r - l <= 6) {
		REP(i,l,r-1)
			REP(j,i+1,r)
				cmin(ret, dis(p[i],p[j]));
		sort(p+l,p+r,[&] (int a,int b) -> bool {
				return y[a] < y[b] || (y[a] == y[b] && x[a] < x[b]);
			});
		return ret;
	}
	int m = (l + r) / 2;
	ll mx = x[m-1] + x[m];
	cmin(ret, min(DC(l,m), DC(m,r)));
	merge(p+l,p+m,p+m,p+r,tmp,[&] (int a,int b) -> bool {
				return y[a] < y[b] || (y[a] == y[b] && x[a] < x[b]);
			});
	copy_n(tmp,r-l,p+l);
	int tp = 0;
	REP(i,l,r)
		if (sqr(2 * x[p[i]] - mx) < ret * 4)
			tmp[tp++] = p[i];
	RP(i,tp-1)
		for (int j = i+1; j < tp && sqr(y[tmp[j]] - y[tmp[i]]) < ret; ++j)
			cmin(ret, dis(tmp[i],tmp[j]));
	return ret;
}
int main()
{
	DRI(n);
	RP1(i,n) {
		p[i] = i;
		x[i] = i;
		RD(y[i]);
		y[i] += y[i-1];
	}
	PL(DC(1,n+1));
}
