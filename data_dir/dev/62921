#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int OO = -2;
const int N = 5003;
vector<pair<int, int>> adj[N];

ll memo[N][N];
int n, t;
ll dp(int node, int remaining) {
	if (remaining == 0) remaining = 1;
	if (node == n - 1) {
		if (remaining == 1) return 0;
		return OO;
	}
	ll &ret = memo[node][remaining];
	if (ret != -1) return ret;
	ret = OO;
	for (auto v : adj[node]) {
		ll tmp = dp(v.first, remaining - 1);
		if (tmp != OO && (tmp + v.second < ret || ret == OO)) {
			ret = tmp + v.second;
		}
	}
	return ret;
}

void print(int node, int remaining) {
	cout << node + 1 << ' ';
	if (remaining == 0) remaining = 1;
	if (node == n - 1) {
		return;
	}
	ll ret = OO, nxt;
	for (auto v : adj[node]) {
		ll tmp = dp(v.first, remaining - 1);
		if (tmp != OO && (tmp + v.second < ret || ret == OO)) {
			ret = tmp + v.second;
			nxt = v.first;
		}
	}
	print(nxt, remaining - 1);
}

void solve() {
	int low = 0, high = N, mid, ans = 0;
	while (low <= high) {
		mid = (low + high) / 2;
		memset(memo, -1, sizeof memo);
		if (dp(0, mid) != OO && dp(0, mid) <= t) {
			ans = mid;
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}
	cout << ans << endl;
	memset(memo, -1, sizeof memo);
	print(0, ans);
}

int main() {
	ios::sync_with_stdio(0), cin.tie(NULL), cout.tie(NULL);
	int m;
	cin >> n >> m >> t;
	while (m--) {
		int u, v, c;
		cin >> u >> v >> c;
		--u, --v;
		adj[u].push_back( { v, c });
	}
	solve();
}