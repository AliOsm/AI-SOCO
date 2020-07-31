#include<bits/stdc++.h>
using namespace std;
#define DEBUG
#ifdef DEBUG
#define debug(...) __f(#__VA_ARGS__, __VA_ARGS__)
	template <typename Arg1>
	void __f(const char* name, Arg1&& arg1){
		cerr << name << " : " << arg1 << std::endl;
	}
	template <typename Arg1, typename... Args>
	void __f(const char* names, Arg1&& arg1, Args&&... args){
		const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
	}
#else
#define debug(...)
#endif
#define FOR(i,a,b) 	for(ll i=a;i<b;++i)
#define RFOR(i,a,b) 	for(ll i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define pii pair<ll,ll>
#define sz(a)	ll(a.size())
#define debug1(x) cout<<x<<endl
#define debug2(x,y) cout<<x<<"-->"<<y<<endl
#define debug3(x,y,z) cout<<x<<"-->"<<y<<"-->"<<z<<endl
typedef long long ll;
typedef long double ld;
const int L = 1e5+7;
ll a[L], n, m, w, au[L], add[L];
bool check(ll val)
{
	FOR(i,0,n)au[i] = a[i], add[i] = 0;
	ll co = 0;
	ll cur;
	FOR(i,0,n-w+1)
	{
		au[i] += add[i];
		add[i+1] += add[i];
		add[i] = 0;
		if(au[i] >= val)continue;
		cur = val - au[i];
		add[i+1] += cur;
		add[i+w] -= cur;
		au[i] += cur;
		co += cur;
	}
	int f = 0;
	std::vector<ll> v;
	FOR(i,n-w+1,n)
	{
		au[i] += add[i];
		add[i+1] += add[i];
		add[i] = 0;
		if(au[i] < val)
		{
			v.pb(val - au[i]);
		}
	}
	sort(v.begin(), v.end());
	if(!v.empty())co += v[sz(v) - 1];
	if(co <= m)return 1;
	return 0;
}
void ser()
{
	ll l=1,r=1e10,mid;
	while(l<r-1)
	{
		mid=(l+r)/2;
		if(check(mid))
			l=mid;
		else r=mid;
	}
	if(!check(r))r=l;
	cout << r;
	return;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	cin >> n >> m >> w;
	 	FOR(i,0,n)cin>>a[i]; 
	 	ser();
		return 0;
}