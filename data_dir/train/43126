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
const int L=1e6+7;
map<int,int> counter;
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
ll size_of_base;
std::vector<int> seg(4*L),lazy(4*L);
void lazyUpdate(int start, int end, int index)
{
	if(lazy[index] != 0)
	{
		seg[index] += lazy[index];
		if(start != end)
		{
			lazy[2*index] += lazy[index];
			lazy[(2*index) + 1] += lazy[index];
		}
		lazy[index] = 0;
	}
	return;
}
void updateRange(int l, int r, ll value, int start = 1, int end = size_of_base, int index = 1)
{
	lazyUpdate(start, end, index);
	if(r < start || l > end || start > end )return;
	if( l <= start && r >= end )
	{
		seg[index] += value;
		if(start != end)
		{
			lazy[2*index] += value;
			lazy[2*index + 1] += value;
		}
		return;
	}
	int mid = (start + end)/2;
	updateRange(l, r, value, start, mid, 2*index );
	updateRange(l, r, value, mid+1, end, 2*index + 1);
	seg[index] = max(seg[2*index] , seg[2*index + 1]) ;
	return;
}
ll query(int l=1, int r=1000000, int start = 1, int end = size_of_base, int index = 1)
{
	lazyUpdate(start, end, index);
	if( start > r || end < l || start > end)
		return 0;
	if(start >= l && end <= r)
		return seg[index];
	int mid = (start + end)/2, query_left, query_right;
	query_left = query(l, r, start, mid, 2*index );
	query_right = query(l, r, mid+1, end, 2*index + 1);
	return max(query_left , query_right);
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int l[5002],r[5002];
	size_of_base =1000000;
	std::vector<int> ans;
	int n;
	cin>>n;
	FOR(i,0,n)
	{
		cin>>l[i]>>r[i];
		if(counter[l[i]]>0)
		{
			if(counter[r[i]]>0)
				updateRange(l[i]+1,r[i]-1,1);
			else
				updateRange(l[i]+1,r[i],1);
		}
		else if(counter[r[i]]>0)
				updateRange(l[i],r[i]-1,1);
		else
		updateRange(l[i],r[i],1);
		counter[r[i]]++;
		counter[l[i]]++;
	}
	FOR(i,0,n)
	{
		updateRange(l[i],r[i],-1);
		int tmp=query();
		// debug2(i,tmp);
		if(tmp==1)ans.pb(i+1);
		updateRange(l[i],r[i],1);
	}
	cout<<sz(ans)<<ln;
	trace(ans,x)cout<<x<<" ";
	return 0;
}