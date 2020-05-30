#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define sz(a)	ll(a.size())
#define debug1(x) cout<<x<<endl
#define debug2(x,y) cout<<x<<"-->"<<y<<endl
#define debug3(x,y,z) cout<<x<<"-->"<<y<<"-->"<<z<<endl
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<ll,ll>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;
const int L=1e5+7;
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
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int n,m,a[100000];
	 	cin >> n >> m;
	 	FOR(i,0,n)cin >> a[i];
	 	int ans=0;
	 	sort(a,a+n);
	 	int mx = a[n-1]+m;
	 	FOR(i,0,n-1)
	 	{
	 		m-=(a[n-1]-a[i]);
	 	}
	 	if(m<=0)
	 	{
	 		cout<<a[n-1]<<" "<<mx;
	 	}
	 	else
	 	{
	 		int ans = a[n-1];
	 		ans += (m/n);
	 		m%=n;
	 		if(m)cout<<ans+1<<" "<<mx;
	 		else cout<<ans<<" "<<mx;
	 	}
		return 0;
}