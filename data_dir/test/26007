#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#define L first
#define V second
using namespace std;
typedef pair<int,int> pii;
const int maxn = 1e5 + 228;
vector<pii> g[maxn];
bool f[maxn];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, k;
	int ans = 2e9;
	cin >> n >> m >> k;
	if (!k)
		goto opt;
	while (m--) {
		int u, v, l;
		cin >> u >> v >> l;
		g[u].emplace_back(l, v);
		g[v].emplace_back(l, u);
	}
	for (int i = 0; i < k; ++i) {
		int a;
		cin >> a;
		f[a] = true;
	}
	for (int i = 1; i <= n; ++i)
		if (f[i])
			for (auto u : g[i]) 
				if (!f[u.V])
					ans = min(ans, u.L);
opt:
	cout << (ans < 2e9 ? ans : -1) << '\n';
}
