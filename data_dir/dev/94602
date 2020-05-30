#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) 	for(ll i=a;i<b;++i)
#define RFOR(i,a,b) 	for(ll i=a;i>=b;--i)
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
const ll L=2e5+7;
ll a[L], tim=1,start[L],ending[L],size_of_base, baseArray[L];
ll depth[L];
std::vector<ll> seg[4*L];
std::vector<pii> v[L];
void dfs(ll vertex, ll parent)
{
	start[vertex] = tim++;
	baseArray[tim-1] = depth[vertex] - a[vertex];
	trace(v[vertex],x)
	{
		if(x.F!=parent)
		{
			depth[x.F] = depth[vertex] + x.S;
			dfs(x.F,vertex);
		}
	}
	ending[vertex] = tim-1;
}
void build(ll start = 1, ll end = size_of_base, ll index = 1)
{
	if( start == end )
	{
		seg[index].pb(baseArray[start]);
		return;
	}
	ll mid = (start + end)/2;
	build(start, mid, 2*index);
	build(mid+1, end, 2*index + 1);
	trace(seg[index<<1],x)seg[index].pb(x);
	trace(seg[(index<<1)+1],x)seg[index].pb(x);
	sort(all(seg[index]));
	return;
}
ll query(ll l, ll r, ll val, ll start = 1, ll end = size_of_base, ll index = 1)
{
	if( start > r || end < l )return 0;
	if(start >= l && end <= r)
	{
		// cout<<val<<" -> ";
		// trace(seg[index],x)cout<<x<<" ";
		// cout<<ln;
		// return 0;
		// cout<<ln;
		// cout<<*upper_bound(all(seg[index]),val)<<ln;
		return (upper_bound(all(seg[index]),val)-seg[index].begin());
	}
	ll mid = (start + end)/2;
	ll query_left, query_right;
	query_left = query(l, r, val,start, mid, 2*index );
	query_right = query(l, r, val, mid+1, end, 2*index + 1);
	return (query_left+ query_right);
}

int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	ll n, aa, bb;
	 	cin >> n;
	 	FOR(i,1,n+1)cin >> a[i];
		FOR(i,2,n+1)
		{
			cin >> aa >> bb;
			v[aa].pb(mp(i,bb));
			v[i].pb(mp(aa,bb));
		}
		dfs(1,-1);
		size_of_base = tim - 1;
		build();
		// FOR(i,1,n+1)debug2(i,depth[i]);
		// FOR(i,1,tim)cout<<baseArray[i]<<" & ";
		// cout<<ln;
		FOR(i,1,n+1)
		{
			// cout<<i<<" -> "<<a[i]+depth[i]<<ln;
			// cou
			cout<<query(start[i],ending[i],depth[i])-1<<" ";
			// query(start[i],ending[i],depth[i]);
			// cout<<ln;
		}
		return 0;
}