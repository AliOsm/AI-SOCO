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

ll fastexp(ll a, ll b){
	ll res = 1LL;
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

const int N = 50+5;
const int MAX = 100+5;
const ll inf = 1LL<<60;

int n;
int m;
int k;
vector<pair<int,pll>> v;
ll memo[N][N][MAX];
int choiceX[N][N][MAX];
int choiceD[N][N][MAX];

pair<ll,int> maximum(int p, int i, int len, ll val){
	pair<ll, int> ans = mp(-inf, -1);
	if(v[i].second.first <= val - k and val - k <= v[i].second.second){
		ans = mp(memo[p][len-1][val - k - v[i].second.first], val - k - v[i].second.first);
	}
	if(val % k == 0 and v[i].second.first <= val / k and val / k <= v[i].second.second){
		if(ans.first < memo[p][len-1][val / k - v[i].second.first]){
			ans = mp(memo[p][len-1][val / k - v[i].second.first], val / k - v[i].second.first);
		}
	}
	return ans;
}

int main(){
	ri3(n, m, k);
	v.resize(m + 1);
	for(int i=1; i<=m; i++){
		rll2(v[i].second.first,v[i].second.second);
		ri(v[i].first);
	}
	v[0].first = -1;
	vi p(m+1);
	iota(all(p),0);
	sort(p.begin(), p.end(), [&](int i, int j){
		return v[i] < v[j];
	});
	for(int x = 1; x <= m; x++){
		int i = p[x];
		for(int l = 1; l <= n; l++){
			for(int d = 0; d <= v[i].second.second - v[i].second.first; d++){
				memo[x][l][d] = l == 1? v[i].second.first + d : -inf;
				if(l == 1) continue;
				for(int y = 1; y < x; y++){
					int j = p[y];
					if(v[j].first == v[i].first) continue;
					pair<ll,int> adding = maximum(y, j, l, d + v[i].second.first);
					if(adding.first > -inf){
						ll cand = adding.first + d + v[i].second.first;
						if(cand > memo[x][l][d]){
							memo[x][l][d] = cand;
							choiceX[x][l][d] = y;
							choiceD[x][l][d] = adding.second;
						}
					}
				}
			}
		}
	}
	int pos = 1;
	int d = 0;
	for(int x=1; x<=m; x++){
		int i = p[x];
		for(int dif = 0; dif <= v[i].second.second - v[i].second.first; dif++){
			if(memo[pos][n][d] < memo[x][n][dif]){
				pos = x;
				d = dif;
			}
		}
	}
	if(memo[pos][n][d] == -inf){
		puts("NO");
		return 0;
	}
	puts("YES");
	stack<pair<int,ll>> S;
	int len = n;
	while(pos > 0){
		S.emplace(mp(p[pos], d + v[p[pos]].second.first));
		int nxtpos = choiceX[pos][len][d];
		int nxtd = choiceD[pos][len][d];
		len -= 1;
		pos = nxtpos;
		d = nxtd;
	}
	while(!S.empty()){
		printf("%d %lld\n",S.top().first,S.top().second);
		S.pop();
	}
	return 0;
}
