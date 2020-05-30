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
#define pii pair<ll,ll>
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
map<pii,ll> counter;
ll fastexpo(ll x,ll y,ll m)
{
	ll temp=1;
	while(y>0)
	{
		if(y&1)temp = ((temp%m)*(x%m))%m;
		x = ((x%m)*(x%m))%m;
		y>>=1;
	}return temp;
}
struct node
{
	int l,r,i;
};
bool comp(node x, node y)
{
	if(x.l == y.l)return x.r < y.r;
	return x.l<y.l;
}
std::vector<node> v;
int co[2];
std::vector<int> ans(L), out(L);
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int t,l,r,n;
	 	cin >> t;
	 	while(t--)
	 	{
	 		cin >> n;
	 		int f1=0;
	 		co[0] = 0, co[1] = 0;
	 		v.clear();
	 		fill(ans.begin(), ans.begin()+n+1,0);
	 		fill(out.begin(), out.begin()+n+1,0);
	 		FOR(i,0,n)
	 		{
	 			cin >> l >> r;
	 			node temp;
	 			temp.l = l,temp.r = r, temp.i = i;
	 			v.pb(temp);
	 		}
	 		sort(all(v),comp);
	 		int cur = v[0].r;
	 		FOR(i,0,n)
	 		{
	 			if(v[i].l<=cur)
	 			{
	 				ans[i] = 1;
	 				cur = max(cur,v[i].r);
	 			}
	 		}
	 		int f=0;
	 		cur= INT_MAX;
	 		FOR(i,0,n)
	 		{
	 			out[v[i].i] = ans[i];
	 			co[ans[i]]++;
	 		}
	 		if(co[0] == n || co[1] == n)
	 		{
	 			cout<<"-1\n";
	 			continue;
	 		}
	 		FOR(i,0,n)cout<<out[i]+1<<" ";
	 		cout<<ln;

	 	}
		return 0;
}