#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
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
map<ll,ll> counter;
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
ll a[100002],cur;
std::vector<pii> ans;
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	ll n;
	 	cin>>n;
	 	FOR(i,0,n){cin>>a[i];a[i]-=i;}
	 	FOR(i,0,n)
	 	{
	 		cur=0;
	 		// debug2(i,i+ceil( (a[i]+n)/n )*n);
	 		if(a[i]<=0)ans.pb(mp(i,i+1));
	 		else ans.pb( mp(i+ceil( (a[i]+n-1)/n )*n,i+1) );
	 		// cout<<i<<" "<<a[i]<<ln;
	 	}
	 	sort(all(ans));
	 	// trace(ans,x)cout<<x.F<<" "<<x.S<<ln;
	 	cout<<(*ans.begin()).S;
		return 0;
}