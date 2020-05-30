#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

void dfs(int u, const vector<vector<int>>& g, vector<int>& vis, vector<double>& val) {
	vis[u] = 1;
	int cnt = 0;
	for (int v : g[u]) {
		if (!vis[v]) {
			++cnt;
			dfs(v, g, vis, val);
			val[u] += (val[v] + 1);
		}
	}
	if (cnt) {
		val[u] /= cnt;
	}
}

int main() {
	int n;
	cin >> n;
	vector<vector<int>> g(n);
	for (int i = 0; i < n - 1; ++i) {
		int u, v;
		cin >> u >> v;
		g[u - 1].push_back(v - 1);
		g[v - 1].push_back(u - 1);
	}
	vector<int> vis(n, 0);
	vector<double> val(n, 0.);
	dfs(0, g, vis, val);
	cout.precision(17);
	cout << std::fixed << val[0] << "\n";
	
	return 0;
}