#include <bits/stdc++.h>
using namespace std;
// iteration
#define CONC(a,b) a ## b
#define CONC_M(a,b) CONC(a,b)
#define __REP(i,s,j,e,nxt) for (auto i = (s), j = (e); i != j; i nxt)
#define _REP(i,s,e,nxt) __REP(i,s,CONC_M(__e,__LINE__),e,nxt)
#define REP(i,s,e) _REP(i,s,e, ++)
#define PER(i,s,e) _REP(i,s,e, --)
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

// Good Luck && Have Fun !

const int maxn = 2.28e5;
char s[maxn];
bool sev[maxn];
int main()
{
	int n,a,b,k;
	scanf("%d%d%d%d%s", &n, &a, &b, &k, s);
	int last = 0;
	REP(i,0,n)
		if (s[i] == '1') {
			REP(j,max(last,i-b+1),i+1)
				sev[j] = true;
			last = i;
		}
	REP(i,n-b+1,n)
		sev[i] = true;
#ifdef PP
	REP(i,0,n)
		printf("%d", sev[i]?1:0);
	puts("");
#endif
	vector<int> p;
	for (int i = n-1; i >= 0; )
		if (!sev[i]) {
			int j = i;
			while (j >= 0 && !sev[j]) {
				if ((i - j) % b == 0)
					p.PB(j);
				--j;
			}
			i = j - 1;
		} else {
			--i;
		}
	int v = SZ(p) - (a - 1);
	printf("%d\n", v);
	REP(i,0,v)
		printf("%d%c", p[i] + 1, i == v - 1 ? '\n' : ' ');
/*
	int ans = (rm + b - 1) / b - a + 1;
	printf("%d\n", ans);
	PER(i,n-1,-1)
		if (!sev[i]) {
			printf("%d%c", i+1, --ans ? ' ' : '\n');
			if (!ans)
				break;
			PER(j,i,max(0,i-b+1)-1)
				sev[j] = true;
		}
*/
}
