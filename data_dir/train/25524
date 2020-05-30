#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5+5, maxk = 18;
int n, m;
int depth[maxn];
int ans[maxn];
int par[maxk][maxn];

int walk(int i, int k) {
	//walks up to k'th ancestor of i
	for (int j = maxk - 1; j >= 0; j--) {
		if (k & (1<<j)) i = par[j][i];
	}
	return i;
}

struct Query
{
	int depth, id;
};
vector<Query> queries[maxn];
vector<int> roots;
string name[maxn]; 

struct Node
{
	vector<set<string>> v; //depths arranged from back of vector
	int sz() { return v.size(); }
	Node() {}
	void addSelf(int i) {
		set<string> add = {name[i]};
		v.push_back(add);
	}
};

void merge(Node& a, Node& b) {
	//merge smaller into the larger
	if (a.sz() < b.sz()) swap(a,b);
	int diff = a.sz() - b.sz();
	for (int i = 0; i < b.sz(); i++) {
		for (string s: b.v[i]) {
			a.v[i+diff].insert(s);
		}
	}
}

vector<int> adj[maxn];
Node* dfs(int i) {
	Node *ni = new Node();
	for (int j: adj[i]) {
		Node *nj = dfs(j);
		merge(*ni,*nj);
	}
	ni->addSelf(i);
	//now answer queries
	for (Query q: queries[i]) {
		int res;
		if (ni->sz()-1-q.depth < 0) res = 0;
		else res = ni->v[ni->sz()-1-q.depth].size();
		ans[q.id] = res;
	}
	return ni;
}

int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> name[i] >> par[0][i];
		if (par[0][i] == 0) {
			//is root
			roots.push_back(i);
		}
		else adj[par[0][i]].push_back(i);
	}
	for (int k = 1; k < maxk; k++) {
		for (int i = 1; i <= n; i++) {
			par[k][i] = par[k-1][par[k-1][i]];
		}
	}
	cin >> m;
	for (int i = 1; i <= m; i++) {
		int v, p; cin >> v >> p;
		queries[v].push_back({p,i});
		//cout << lc << ' ' << p << '\n';
	}
	for (int i: roots) {
		dfs(i);
	}
	//output
	for (int i = 1; i <= m; i++) {
		cout << ans[i] << '\n';
	}
}