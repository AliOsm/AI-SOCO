#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds; 
#define ii pair<int,int>
#define ll long long
#define pll pair<ll,ll>
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update> 
#define iiordered_set tree<pll, null_type,less<pll>, rb_tree_tag,tree_order_statistics_node_update>
using namespace std;
#define MOD 1000000007
ll power(ll a,ll b, ll m=MOD)
{
    ll res=1;
    while(b>0)
    {
        if(b&1)
            res=(res*a)%m;
        a=(a*a)%m;
        b>>=1;
    }
    return res%m;
}
ll inverse(ll a,ll m=MOD)
{
    return power(a,m-2,m);
}
#define INFl 1e18
#define vi vector<int>
#define vvi vector<vi>
#define vl vector<long long>
#define vvl vector<vl>
#define vii vector<ii>
#define vvii vector<vii>
#define F first
#define S second
#define forl(i,n) for(int i=0;i<n;i++)
#define fore(i,n) for(int i=1;i<=n;i++)
#define rforl(i,n)  for(int i=n-1;i>=0;i--)
#define rfore(i,n)  for(int i=n;i>=1;i--)
#define CASE(t) cout<<"Case #"<<(t)<<": ";
#define INF 1100000009
#define gcd(a,b) __gcd(a,b)
#define all(x)  x.begin(),x.end()
#define mp make_pair
#define pb push_back
#define print(x)    for(auto it=x.begin();it!=x.end();it++) cout<<*it<<' '; cout<<endl;
#define printii(x)  for(auto it=x.begin();it!=x.end();it++) cout<<it->F<<' '<<it->S<<endl;  
#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 
ll manhat(ll a,ll b,ll x2,ll y2)
{
	return abs(x2-a)+abs(y2-b);
}
ll g[2005][2005];
int main()
{
	fastio;
	int n;
	cin>>n;
	vl x(n),y(n);
	forl(i,n)	cin>>x[i]>>y[i];
	vl c(n),k(n);
	forl(i,n)	cin>>c[i];
	forl(i,n)	cin>>k[i];
	forl(i,n)
	{
		for(int j=i;j<n;j++)
		{
			g[j][i]=g[i][j]=manhat(x[i],y[i],x[j],y[j])*(k[i]+k[j]);
		}
	}
	vi vis(n,-1);
	vl dist(n,INFl);
	vl parent(n,n);
	forl(i,n)
		dist[i]=c[i];
	ll ans=0;
	forl(i,n)
	{
		ll idx=-1,mn=INFl;
		forl(j,n)
		{
			if(dist[j]<mn && vis[j]==-1)
			{
				mn=dist[j];
				idx=j;
			}
		}
		ans+=mn;
		vis[idx]=parent[idx];
		forl(j,n)
		{
			if(dist[j]>g[idx][j])
			{
				parent[j]=idx;
				dist[j]=g[idx][j];
			}
		}
	}
	cout<<ans<<endl;
	vi pows;
	vii edge;
	forl(i,n)
	{
		if(vis[i]==n)
			pows.pb(i+1);
		else
		{
			edge.pb(mp(i+1,vis[i]+1));
		}
	}
	cout<<pows.size()<<endl;
	print(pows);
	cout<<edge.size()<<endl;
	printii(edge);
}
