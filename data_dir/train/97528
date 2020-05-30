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
ll power[20],ans=INT_MIN;
std::map<ll, int> counter;
void solve(int n,int numdig)
{
	if(n==0 || counter.find(n)!=counter.end())return;
	counter[n]++;
	if(ceil(sqrt(n)) == floor(sqrt(n)))
	{
		if(ans<numdig)
		ans=numdig;
		return;
	}
	if(numdig==1)return;
	ll tmp;
	FOR(i,1,numdig+1)
	{
		tmp=n/power[i];
		solve(tmp*power[i-1]+n%power[i-1],numdig-1);
	}
	return;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	ll tmp,n,co=0;
	 	cin>>n;
	 	tmp=n;
	 	while(tmp>0)
	 	{
	 		co++;
	 		tmp/=10;
	 	}
	 	power[0]=1;
	 	FOR(i,1,11)power[i]=power[i-1]*10;
	 	solve(n,co);
	 	if(ans!=INT_MIN)cout<<co-ans;
	 	else cout<<"-1";
		return 0;
}