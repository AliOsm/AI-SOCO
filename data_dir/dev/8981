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
#define pii pair<int,int>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;
const int L=1e5+7;
pii adj[L];
int pa[L], val[L], ans=0;
std::map<int, int> counter;
void dfs(int vertex, int l, int r)
{
	// debug3(val[vertex],l,r);
	if(val[vertex]>=l && val[vertex]<=r)
		ans+=counter[val[vertex]];
	if(adj[vertex].F != -1)
		dfs(adj[vertex].F, l, min(val[vertex]-1,r));
	if(adj[vertex].S != -1)
		dfs(adj[vertex].S, max(l,val[vertex]+1), r);
	return;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int n, l, r, v;
	 	cin >> n;
	 	FOR(i,1,n+1)
	 	{
	 		cin >> v >> l >> r;
	 		val[i] = v;
	 		adj[i].F = l;
	 		adj[i].S = r;
	 		pa[l] = i;
	 		pa[r] = i;
	 		counter[v]++;
	 	}
	 	FOR(i,1,n+1)
	 		if(!pa[i])
	 			dfs(i,INT_MIN,INT_MAX);
	 	cout<<n-ans;
		return 0;
}