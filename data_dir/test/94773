#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define DEBUG
#ifdef DEBUG
#define debug(...) __f(#__VA_ARGS__, __VA_ARGS__)
	template <typename Arg1>
	void __f(const char* name, Arg1&& arg1){
		cerr << name << " : " << arg1 << std::endl;
	}
	template <typename Arg1, typename... Args>
	void __f(const char* names, Arg1&& arg1, Args&&... args){
		const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
	}
#else
#define debug(...)
#endif
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define sz(a)	int(a.size())
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<ll,ll>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
// ordered_set X
//K-th smallest
//*X.find_by_order(k-1)
//NO OF ELEMENTS < A
//X.order_of_key(A)

const int L=1e6+7;
struct node
{
	int to, idx;
	int flow, capacity;
};
std::vector<node> v[L];
std::vector<int> ptr(L), dist(L);
std::map<string, int> val;
std::map<int, string> val1;
void addEdge(int s, int t, int capacity)
{
	node a = {t, sz(v[t]), 0, capacity};
	node b = {s, sz(v[s]), 0, capacity};
	v[s].pb(a);
	v[t].pb(b);
}
int dfs(int vertex, int flow, int dest)
{
	if(vertex == dest)return flow;
	int df;
	node x;
	for(;ptr[vertex] < sz(v[vertex]);ptr[vertex]++)
	{
		x = v[vertex][ptr[vertex]];
		if(dist[x.to] == dist[vertex] + 1 && x.flow < x.capacity)
		{
			df = dfs(x.to, min(flow, x.capacity - x.flow), dest);
			if(df > 0)
			{
				v[vertex][ptr[vertex]].flow += df;
				v[x.to][x.idx].flow -= df;
				return df;
			}
		}
	}
	return 0;
}
bool bfs(int src,int  dest, int number_of_nodes)
{
	fill(dist.begin(), dist.begin() + number_of_nodes + 1, -1);
	int tmp;
	queue<int>q;
	q.push(src);
	dist[src] = 0;
	while(!q.empty())
	{
		tmp = q.front();
		q.pop();
		trace(v[tmp], x)
		{
			if(dist[x.to] == -1 && x.flow < x.capacity)
			{
				dist[x.to] = dist[tmp] + 1;
				q.push(x.to);
			}
		}
	}
	return dist[dest] == -1 ? 0 : 1; 
}
ll maxFlow(int source, int destination, int number_of_nodes)
{
	if(source == destination)return -1;
	ll ans = 0, delta;
	while(bfs(source, destination, number_of_nodes))
	{
		fill(ptr.begin(), ptr.begin() + number_of_nodes, 0);
		while(delta = dfs(source, INT_MAX, destination))
		{
			ans += delta;
		}
	}
	return ans;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int a, b, c, src, dest, n, len;
	 	int sm, m, l, xl, xxl, xxxl;
	 	cin >> sm >> m >> l >> xl >> xxl >> xxxl;
	 	cin >> n;
	 	addEdge(n+1, n+7, sm);
	 	addEdge(n+2, n+7, m);
	 	addEdge(n+3, n+7, l);
	 	addEdge(n+4, n+7, xl);
	 	addEdge(n+5, n+7, xxl);
	 	addEdge(n+6, n+7, xxxl);
	 	string s;
	 	val["S"] = n + 1;
	 	val["M"] = n + 2;
	 	val["L"] = n + 3;
	 	val["XL"] = n + 4;
	 	val["XXL"] = n + 5;
	 	val["XXXL"] = n + 6;
	 	val1[n+1] = "S";
	 	val1[n+2] = "M";
	 	val1[n+3] = "L";
	 	val1[n+4] = "XL";
	 	val1[n+5] = "XXL";
	 	val1[n+6] = "XXXL";
	 	int cur = 0;
	 	
	 	FOR(i,1,n+1)
	 	{
	 		cin >> s;
	 		len = s.length();
	 		cur = -1;
	 		FOR(j,0,len)
	 		{
	 			if(s[j] == ',')
	 			{
	 				cur = j;
	 				break;
	 			}
	 		}
	 		addEdge(0, i, 1);
	 		if(cur == -1)addEdge(i, val[s], 1);
	 		else
	 		{
	 			addEdge(i, val[s.substr(0,cur)], 1);
	 			addEdge(i, val[s.substr(cur+1,len-cur)], 1);
	 		}
	 	}	
	 	src = 0, dest = n + 7;
	 	cur = maxFlow(src, dest, n+8);
	 	if(cur < n)
	 	{
	 		cout<<"NO\n";
	 	}
	 	else
	 	{
	 		cout<<"YES\n";
	 		FOR(i,1,n+1)
	 		{
	 			trace(v[i], x)
	 			{
	 				if(x.flow == 1)
	 				{
	 					cout<<val1[x.to]<<ln;
	 				}
	 			}
	 		}
	 	}
		return 0;
}