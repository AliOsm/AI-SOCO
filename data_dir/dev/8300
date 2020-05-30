#include<bits/stdc++.h>
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define ri(x) scanf("%d",&(x))
#define ri2(x,y) scanf("%d %d",&(x),&(y))
#define ri3(x,y,z) scanf("%d %d %d",&(x),&(y),&(z))
#define rll(x) scanf("%lld",&(x))
#define rll2(x,y) scanf("%lld %lld",&(x),&(y))
#define rll3(x,y,z) scanf("%lld %lld %lld",&(x),&(y),&(z))
#define gc(x) ((x) = getchar())
using namespace::std;

const long double PI = acos(-1);
const long long MOD = 1000000000 +7;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<ll,pll> tll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef vector<tll> vtll;
typedef vector<string> vs;
typedef set<int> si;
typedef set<ii> sii;
typedef set<iii> siii;

ll gcd(ll a, ll b){ return b==0?a:gcd(b,a%b);}

ll add(ll a, ll b, ll m = MOD){
	if(a >= m) a %= m;
	if(b >= m) b %= m;
	if(a < 0) a += m;
	if(b < 0) b += m;
	ll res = a+b;
	if(res >= m or res <= -m) res %= m;
	if(res < 0) res += m;
	return res;
}

ll mul(ll a, ll b, ll m = MOD){
	if(a >= m) a %= m;
	if(b >= m) b %= m;
	if(a < 0) a += m;
	if(b < 0) b += m;
	ll res = a*b;
	if(res >= m or res <= -m) res %= m;
	if(res < 0) res += m;
	return res;
}

ll pow_mod(ll a, ll b, ll m = MOD){
	ll res = 1LL;
	a = a%m;
	while(b){
		if(b&1) res = mul(res,a,m);
		b >>= 1;
		a = mul(a,a,m);
	}
	return res;
}

ull fastexp(ull a, ll b){
	ull res = 1;
	while(b){
		if(b&1) res = res*a;
		b >>= 1;
		a *= a;
	}
	return res;
}

int gcdExtendido(int a, int b, int *x, int *y){
	if(a == 0){
		*x = 0;
		*y = 1;
		return b;
	}
	int x1, y1;
	int gcd = gcdExtendido(b%a,a,&x1,&y1);
	
	*x = y1-(b/a)*x1;
	*y = x1;
	return gcd;
}

int modInverso(int a, int m){
	int x, y;
	int g = gcdExtendido(a,m,&x,&y);
	if(g!=1) return -1;
	else return (x%m + m)%m;
}

/****************************************
*************P*L*A*N*T*I*L*L*A************
*****************************************/

const int N = 5000+5;

int n;
int a;
int b;
string s;

vector<int> getZ(string &pattern){
	int m = pattern.size();
	int l = 0;
	int r = 0;
	vector<int> zp(m,0);
	for(int i=1; i<m; i++){
		zp[i] = min(r-i,zp[i-l]);
		if(zp[i] < 0) zp[i] = 0;
		while(i + zp[i] < m and pattern[zp[i]] == pattern[i+zp[i]]) zp[i]++;
		if(r < i + zp[i] - 1){
			l = i;
			r = i + zp[i] - 1;
		}
	}
	return zp;
}

int getPossible(int len){
	string act = s.substr(0, len);
	reverse(all(act));
	vector<int> z = getZ(act);
	int res = 0;
	for(int i = 0; i < z.size(); i++){
		int here = min(i, z[i]);
		res = max(res, here);
	}
	return res;
}

int solve(){
	vector<int> memo(n + 1, 0);
	for(int i = 1; i <= n; i++){
		memo[i] = memo[i-1] + a;
		int possible = getPossible(i);
		for(int l = 1; l <= possible; l++){
			memo[i] = min(memo[i], memo[i - l] + b);
		}
	}
	return memo[n];
}

int main(){
	cin >> n >> a >> b >> s;
	int ans = solve();
	printf("%d\n",ans);
	return 0;
}
