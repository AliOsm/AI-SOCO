#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> g[5005];
vector<int> req[5005];
int ans[5005];

int to, mn;
bool dfs1(int now, int pa) {
	if (now == to) return 1;
	for (pair<int, int> &i : g[now]) if (i.first != pa) {
		if (dfs1(i.first, now)) {
			req[i.second].push_back(mn);
			return 1;
		}
	}
	return 0;
}

vector<int> ids;
bool dfs2(int now, int pa) {
	if (now == to) return 1;
	for (pair<int, int> &i : g[now]) if (i.first != pa) {
		if (dfs2(i.first, now)) {
			ids.push_back(i.second);
			return 1;
		}
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n; cin >> n;
	for (int i = 1; i < n; ++i) {
		int u, v; cin >> u >> v;
		g[u].emplace_back(v, i);
		g[v].emplace_back(u, i);
		ans[i] = 902131;
	}

	int m; cin >> m;
	vector<tuple<int, int, int>> zzz;
	while (m--) {
		int u, v, f; cin >> u >> v >> f;
		zzz.emplace_back(f, u, v);
	}
	sort(zzz.begin(), zzz.end());

	for (auto& [f, u, v] : zzz) {
		to = v, mn = f;
		dfs1(u, 0);
	}

	for (int i = 1; i < n; ++i) reverse(req[i].begin(), req[i].end());

	for (auto [f, u, v] : zzz) {
		ids.clear();
		to = v, mn = f;
		dfs2(u, 0);
		bool ok = false;
		for (int ei : ids) {
			if (req[ei][0] == f) {
				ok = true;
				ans[ei] = f;
			}
		}
		if (!ok) {
			exit((cout << -1 << endl, 0));
		}
		for (int ei : ids) {
			req[ei].pop_back();
		}
	}

	for (int i = 1; i < n; ++i) cout << ans[i] << ' ';
	cout << endl;
}
