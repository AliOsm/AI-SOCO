#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
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
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define sz(a)	ll(a.size())
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<int,int>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
// ordered_set X
//K-th smallest
//*X.find_by_order(k-1)
//NO OF ELEMENTS < A
//X.order_of_key(A)

const int L=1e6+7;
map<ll,ll> counter;
std::vector<pii> v;
int N;
bool check(int n)
{
	if(n >= N)return 0;
	std::vector<pii> cur;
	int l, r;
	trace(v,x)
	{
		l = (x.F + n) % N;
		r = (x.S + n) % N;
		if(l > r)swap(l, r);
		cur.pb(mp(l, r));
	}
	sort(all(cur));
	if(cur == v)return 1;
	return 0;
}
bool solve(int n)
{
	int tmp = sqrt(n) + 1;
	FOR(i,1,tmp)
	{
		if(n%i == 0)
		{
			if(check(i))return 1;
			if(n != i*i)
			{
				if(check(n/i))return 1;
			}
		}
		
	}
	return 0;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int M, a, b, diff;
	 	cin >> N >> M;
	 	FOR(i,0,M)
	 	{
	 		cin >> a >> b;
	 		a--, b--;
	 		if(a>b)swap(a,b);
	 		v.pb(mp(a,b));
	 	}
	 	sort(all(v));
	 	if(solve(N))cout<<"Yes\n";
	 	else cout<<"No\n";
		return 0;
}