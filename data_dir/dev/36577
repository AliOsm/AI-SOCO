#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")

#define pb push_back
#define mp make_pair
#define sz(a) (ll)(a).size()

#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp> // Including tree_order_statistics_node_update

using namespace __gnu_pbds;
typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
//K-th smallest
//cout << k << "rd smallest: " << *A.find_by_order(k-1) << endl;
//NO OF ELEMENTS < X
//cout << "No of elements less than " << X << " are " << A.order_of_key(X) << endl;


typedef long long ll;
typedef pair<ll,ll> pii;

ll mod=1000000007;

ll power(ll x, ll y) 
{
	ll temp;
	if( y == 0)
		return 1;
	temp = power(x, y/2);
	if (y%2 == 0)
		return (temp*temp)%mod;
	else
		return (((x*temp)%mod)*temp)%mod; 
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll n;
	cin>>n;
	vector<ll> b,c,d;
	ll ans=0;
	ll curCnt=0;
	ll i;
	for(i=0;i<n;i++)
	{
		string s;
		ll val;
		cin>>s>>val;
		if(s=="11")
		{
			ans+=val;
			curCnt++;
		}
		else if(s=="10")
			b.pb(val);
		else if(s=="01")
			c.pb(val);
		else
			d.pb(val);
	}
	sort(b.begin(),b.end());
	sort(c.begin(),c.end());
	reverse(b.begin(),b.end());
	reverse(c.begin(),c.end());
	for(i=0;i<min(sz(b), sz(c));i++)
	{
		ans+=b[i];
		ans+=c[i];
	}
	while(i<sz(b))
	{
		d.pb(b[i]);
		i++;
	}
	i=min(sz(b), sz(c));
	while(i<sz(c))
	{
		d.pb(c[i]);
		i++;
	}
	sort(d.begin(),d.end());
	reverse(d.begin(),d.end());
	i=0;
	while(curCnt-- && i<sz(d))
	{
		ans+=d[i];
		i++;
	}
	cout<<ans<<endl;
	return 0;
}