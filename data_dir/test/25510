#include <bits/stdc++.h>
using namespace std;
// iteration
#define CONC(a,b) a ## b
#define CONC_M(a,b) CONC(a,b)
#define __REP(i,s,j,e,nxt) for (auto i = (s), j = (e); i != j; i nxt)
#define _REP(i,s,e,nxt) __REP(i,s,CONC_M(__e,__LINE__),e,nxt)
#define REP(i,s,e) _REP(i,s,e, ++)
#define RP(i,n) REP(i,0,n)
#define PER(i,s,e) _REP(i,s,e, --)
#define PR(i,n) PER(i,n-1,-1)
#define REP_B(i,e) _REP(i,1,e, <<= 1)
#define DO(n) REP(CONC_M(__i,__LINE__),0,n)

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
bool RD(char * a) {return scanf("%s", a) == 1;}
template<typename T, typename ... TT>
bool RD(T & a, TT & ...  b) {return RD(a) && RD(b...);}

/* Good Luck && Have Fun ! */

const int maxn = 4026;
const int maxk = sqrt(2 * maxn);
int n;
int a[maxn];
int dp[maxn][maxk][maxk];
bool vis[maxn][maxk][maxk];

/*
dp(l,d,k) = 
		max(
			min(
				dp(l+k,d,k) + (a[l+k] - a[l]) - (a[n-d-l] - a[n-d-l-k]), 
				dp(l+k,d+1,k+1) + (a[l+k] - a[l]) - (a[n-d-l] - a[n-d-l-k-1])
			),
			min(
				dp(l+k+1,d,k+1) + (a[l+k+1] - a[l]) - (a[n-d-l] - a[n-d-l-k-1]), 
				dp(l+k+1,d+1,k+2) + (a[l+k+1] - a[l]) - (a[n-d-l] - a[n-d-l-k-2])
			)
		);
*/

int calc(int l, int d, int k)
{
	if (vis[l][d][k])
		return dp[l][d][k];
	vis[l][d][k] = true;
	int wid = n-l-d - l;
	int & now = dp[l][d][k];
	if (wid < k){
		return now = 0;
	} else if (wid < 2 * k) {
		now = a[l+k] - a[l];
		if (wid >= k + 1)
			now = max(now, a[l+k+1] - a[l]);
		return now;
	} else {
		int v0 = calc(l+k,d,k) + (a[l+k] - a[l]) - (a[n-d-l] - a[n-d-l-k]);
		if (wid >= 2 * k + 1)
			v0 = min(v0, calc(l+k,d+1,k+1) + (a[l+k] - a[l]) - (a[n-d-l] - a[n-d-l-k-1]));
		now = v0;
		if (wid >= 2 * k + 2) {
			int v1 = calc(l+k+1,d,k+1) + (a[l+k+1] - a[l]) - (a[n-d-l] - a[n-d-l-k-1]); 
			if (wid >= 2 * k + 3)
				v1 = min(v1, calc(l+k+1,d+1,k+2) + (a[l+k+1] - a[l]) - (a[n-d-l] - a[n-d-l-k-2]));
			now = max(now, v1);
		} else {
			now = max(now, a[l+k+1] - a[l]);
		}
	}
	return now;
}

int main()
{
	RD(n);
	REP(i,1,n+1) {
		RD(a[i]);
		a[i] += a[i-1];
	}
	printf("%d\n", calc(0,0,1));
}
