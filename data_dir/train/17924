#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
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
#define sz(a)	ll(a.size())
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<ll,ll>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;

typedef tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update> pbds;
// ordered_set X
//K-th smallest
//*X.find_by_order(k-1)
//NO OF ELEMENTS < A
//X.order_of_key(A)

const ll L=2e5+7;
ll dp[L][12];
ll n;
std::vector<ll> v[L][4];
inline ll f(ll x)
{
	return ((x%10 == 0)?2:1);
}
ll solve(ll i, ll sofar)
{
	if(i>n)return 0;
	if(dp[i][sofar])return dp[i][sofar];
	ll ret = solve(i+1, sofar);
	FOR(j,1,4)
	{
		if(sz(v[i][j]) == 0)continue;
		ret = max(ret, f(sofar+1)*v[i][j][sz(v[i][j])-1] + solve(i+1, (sofar+1)%10));
	}
	if(sz(v[i][1]) >= 2)
	{
		ret = max(ret, f(sofar+1)*v[i][1][sz(v[i][1])-1] + f(sofar+2)*v[i][1][sz(v[i][1])-2] + solve(i+1, (sofar+2)%10));
		ret = max(ret, f(sofar+2)*v[i][1][sz(v[i][1])-1] + f(sofar+1)*v[i][1][sz(v[i][1])-2] + solve(i+1, (sofar+2)%10));
	}
	if(sz(v[i][1]) >= 3)
	{
		ret = max(ret, f(sofar+1)*v[i][1][sz(v[i][1])-1] + f(sofar+2)*v[i][1][sz(v[i][1])-2] + f(sofar+3)*v[i][1][sz(v[i][1])-3]+ solve(i+1, (sofar+3)%10));
		ret = max(ret, f(sofar+1)*v[i][1][sz(v[i][1])-1] + f(sofar+3)*v[i][1][sz(v[i][1])-2] + f(sofar+2)*v[i][1][sz(v[i][1])-3]+ solve(i+1, (sofar+3)%10));
		ret = max(ret, f(sofar+2)*v[i][1][sz(v[i][1])-1] + f(sofar+1)*v[i][1][sz(v[i][1])-2] + f(sofar+3)*v[i][1][sz(v[i][1])-3]+ solve(i+1, (sofar+3)%10));
		ret = max(ret, f(sofar+2)*v[i][1][sz(v[i][1])-1] + f(sofar+3)*v[i][1][sz(v[i][1])-2] + f(sofar+1)*v[i][1][sz(v[i][1])-3]+ solve(i+1, (sofar+3)%10));
		ret = max(ret, f(sofar+3)*v[i][1][sz(v[i][1])-1] + f(sofar+1)*v[i][1][sz(v[i][1])-2] + f(sofar+2)*v[i][1][sz(v[i][1])-3]+ solve(i+1, (sofar+3)%10));
		ret = max(ret, f(sofar+3)*v[i][1][sz(v[i][1])-1] + f(sofar+2)*v[i][1][sz(v[i][1])-2] + f(sofar+1)*v[i][1][sz(v[i][1])-3]+ solve(i+1, (sofar+3)%10));
	}
	if(sz(v[i][1]) >= 1 && sz(v[i][2]) >= 1)
	{
		ret = max(ret, f(sofar+1)*v[i][1][sz(v[i][1])-1] + f(sofar+2)*v[i][2][sz(v[i][2])-1] + solve(i+1, (sofar+2)%10));
		ret = max(ret, f(sofar+2)*v[i][1][sz(v[i][1])-1] + f(sofar+1)*v[i][2][sz(v[i][2])-1] + solve(i+1, (sofar+2)%10));
	}
	return dp[i][sofar] = ret;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	cin >> n;
	 	ll c, d, k;
	 	FOR(i,1,n+1)
	 	{
	 		cin >> k;
	 		while(k--)
	 		{
	 			cin >> c >> d;
	 			v[i][c].pb(d);
	 		}
	 		FOR(j,1,4)sort(all(v[i][j]));
	 	}
	 	cout<<solve(1,0);
		return 0;
}