#include<bits/stdc++.h>
using namespace std;
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
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;
ll mark[200002],newar[200002];
std::vector<ll> inp;
std::vector<pii> v;
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
		ll l,r,n,q,a;
		cin>>n>>q;
		FOR(i,0,n){cin>>a;inp.pb(a);}
		while(q--)
		{
			cin>>l>>r;
			mark[l]++,mark[r+1]--;
		}
		FOR(i,1,n+1)mark[i]+=mark[i-1];
		FOR(i,1,n+1)
			v.pb(mp(mark[i],i));
		sort(v.rbegin(),v.rend());
		sort(inp.rbegin(),inp.rend());
		ll cur=0;
		trace(v,x)
			newar[x.S]=inp[cur++];
		ll ans=0;
		FOR(i,1,n+1)
			ans+=mark[i]*newar[i];
		cout<<ans;
		return 0;
}