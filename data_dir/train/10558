#include <bits/stdc++.h>
using namespace std;
// #include </home/edison/Coding/cpp/template/debug.cpp>

int t[100005];
long long ans[100005];

int main() {
	int n, p; cin >> n >> p;
	for (int i = 1; i <= n; ++i) cin >> t[i];

	priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> want_go, want_back;
	for (int i = 1; i <= n; ++i) want_go.emplace(t[i], i);

	long long nt = 0, can_start = 0;
	set<int> not_sit, can_go;
	int cnt = 0;
	
	while (cnt < n) {
		// PDE(cnt, nt, can_start, want_go, want_back, not_sit, can_go);
		if (!want_go.size() || (want_back.size() && want_back.top().first < want_go.top().first)) {
			int now = want_back.top().second;
			nt = want_back.top().first;
			want_back.pop();
			not_sit.erase(now);
			++cnt;

			if (can_go.size() && not_sit.lower_bound(*can_go.begin()) == not_sit.begin()) {
				now = *can_go.begin();
				can_go.erase(can_go.begin());
				not_sit.insert(now);
				can_start = max(nt, can_start) + p;
				ans[now] = can_start;
				// PDE(now, ans[now]);
				want_back.emplace(ans[now], now);
			}
		} else {
			int now = want_go.top().second;
			nt = want_go.top().first;
			want_go.pop();
			
			if (not_sit.lower_bound(now) == not_sit.begin()) {
				can_start = max(nt, can_start) + p;
				ans[now] = can_start;
				// PDE(now, ans[now]);
				want_back.emplace(ans[now], now);
				not_sit.insert(now);
			} else {
				can_go.insert(now);
			}
		}
	}

	for (int i = 1; i <= n; ++i) cout << ans[i] << ' ';
	cout << endl;
}
