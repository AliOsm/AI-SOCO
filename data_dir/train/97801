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
typedef long long ll;
typedef long double ld;
const int L=1e5+7;
set<int>v[L];
int depth[L],parent[L][22],subtree[L],centroidParent[L],ans[L];
std::vector<int> distanceis(L,INT_MAX/4);
vector<int>adj[L];
int final;
void dfs(int vertex,int prev,int level)
{
	depth[vertex]=level+1;
	final=level+1;
	parent[vertex][0]=prev;
	for(auto &x:v[vertex])
		if(x!=prev)dfs(x,vertex,level+1);
}
void solve(int vertex,int prev,int level)
{
	ans[vertex]=level+1;
	for(auto &x:adj[vertex])
	{
		if(x!=prev)
			solve(x,vertex,level+1);
	}
}
int size(int vertex,int prev)
{
	subtree[vertex]=1;
	for(auto &x:v[vertex])
	{
		if(x!=prev)
			subtree[vertex]+=size(x,vertex);
	}
	return subtree[vertex];
}
int findCentroid(int vertex,int prev,int n)
{
	for(auto &x:v[vertex])
	{
		if(x!=prev && subtree[x]>n/2)
			return findCentroid(x,vertex,n);
	}
	return vertex;
}
void decompose(int vertex,int prev)
{
	size(vertex,-1);
	int c=findCentroid(vertex,-1,subtree[vertex]);
	centroidParent[c]=prev;
	for(auto &x:v[c])
	{
		v[x].erase(c);
		decompose(x,c);
	}
	v[c].clear();
	return;
}
int lca(int u,int v)
{
	if(depth[u]>depth[v])swap(u,v);
	int dist=depth[v]-depth[u];
	int index=0;
	while(dist>0)
	{
		if(dist&1)v=parent[v][index];
		index++;
		dist>>=1;
	}
	RFOR(i,18,0)
	{
		if(parent[u][i]!=-1 && parent[u][i]!=parent[v][i])
		{
			u=parent[u][i];
			v=parent[v][i];
		}
	}
	if(u==v)return u;
	return parent[u][0];
}
int findDistance(int u,int v)
{
	return depth[u]+depth[v]-2*depth[lca(u,v)];
}
void update(int vertex)
{
	int cur=vertex;
	while(cur!=-1)
	{
		distanceis[cur]=min(distanceis[cur],findDistance(cur,vertex));
		cur=centroidParent[cur];
	}
	return;
}
int query(int vertex)
{
	int cur=vertex,ans=INT_MAX;
	while(cur!=-1)
	{
		ans=min(ans,distanceis[cur]+findDistance(cur,vertex));
		cur=centroidParent[cur];
	}
	return ans;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int type,n,m,a,b;
	 	cin>>n;
	 	FOR(i,0,n-1)
	 	{
	 		cin>>a>>b;
	 		v[a].insert(b);
	 		v[b].insert(a);
	 	}
	 	FOR(i,1,n+1)
	 	{
	 		centroidParent[i]=-1;
	 		FOR(j,0,20)
	 		parent[i][j]=-1;
	 	}
	 	dfs(1,-1,-1);
	 	FOR(j,1,19)FOR(i,1,n+1)
	 		if(parent[i][j-1]!=-1)
	 			parent[i][j]=parent[parent[i][j-1]][j-1];
		decompose(1,-1);
		int root;
		FOR(i,1,n+1)
		{
			if(centroidParent[i]!=-1)
			{
				adj[i].pb(centroidParent[i]);
				adj[centroidParent[i]].pb(i);
			}
			else 
				root=i;
		}
		solve(root,-1,-1);
		// cout<<final<<endl;
		// if(final>26)cout<<"-1";
		// else
		{
			FOR(i,1,n+1)
				cout<<char(65+ans[i])<<" ";
		}
		return 0;

}