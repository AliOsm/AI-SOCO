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
#define all(c)	c.begin(),c.end()
#define debug3(x,y,z) cout<<x<<"-->"<<y<<"-->"<<z<<endl
typedef long long ll;
typedef long double ld;
map<ll,ll> counter;
int n;
std::vector<int> v;
bool check(ll val)
{
	int ar[102];
	int cur=0,f=0,cycle=0,idx=0;
	FOR(i,0,101)ar[i]=INT_MAX;
	// cout<<val<<"-";
	while(cur<n)
	{
		if(ar[idx]==0)
		{
			idx++;
			if(idx==val)
			{
				idx=0;
				if(!cycle)return 0;
				cycle=0;
			}
			continue;
		}
		ar[idx]=min(ar[idx]-1,v[cur]);
		// cout<<ar[idx]<<" ";
		cycle=1;
		cur++;
		idx++;
		if(idx==val)idx=0,cycle=0;
	}
	return 1;
}
void ser()
{
	ll l=1,r=100,mid;
	while(l<r-1)
	{
		mid=(l+r)/2;
		if(check(mid))
			r=mid;
		else l=mid;
		// cout<<ln;
	}
	if(!check(l))l=r;
	cout<<l;
	// cout<<l<<" "<<r<<" "<<mid<<ln;
	return;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	cin>>n;
	 	int a;
	 	FOR(i,0,n){cin>>a;v.pb(a);}
	 	sort(all(v));
	 	reverse(all(v));
	 	// FOR(i,0,n)cout<<v[i]<<" ";
	 	ser();
		return 0;
}