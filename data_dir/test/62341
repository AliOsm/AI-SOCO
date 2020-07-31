#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;

string mp[505];
int dp1[505][505], dp2[505][505], dp3[505][505], dp4[505][505];
int sz1[505][505], sz2[505][505], sz3[505][505], sz4[505][505];
int pre[505][505];
int ans[300005];
vector<pair<int, int>> at[505];

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n, m, q; cin >> n >> m >> q;
	for (int i = 0; i < n; ++i) cin >> mp[i];

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			int mx = 0;
			if (mp[i][j] == 'R') {
				mx = 1;
				for (int k = 1; ; ++k) {
					if (k > i || k > j) break;
					if (sz1[i - 1][j] >= k && sz1[i][j - 1] >= k && mp[i - k][j - k] == 'R') ++mx;
				}
			}
			dp1[i][j] = mx;
			sz1[i][j] = mx;
		}
	}

	// cerr << "dp1:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << dp1[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }
	// cerr << "sz1:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << sz1[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }

	for (int i = 0; i < n; ++i) {
		for (int j = 1; j < m; ++j) {
			int mx = 0;
			if (mp[i][j] == 'G') {
				mx = 1;
				for (int k = 1; ; ++k) {
					if (k > i || k > j) break;
					if (sz2[i - 1][j] >= k && sz2[i][j - 1] >= k && mp[i - k][j - k] == 'G') ++mx;
				}
			}
			dp2[i][j] = min(mx, dp1[i][j - mx]);
			sz2[i][j] = mx;
		}
	}

	// cerr << "dp2:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << dp2[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }
	// cerr << "sz2:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << sz2[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }

	for (int i = 1; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			int mx = 0;
			if (mp[i][j] == 'Y') {
				mx = 1;
				for (int k = 1; ; ++k) {
					if (k > i || k > j) break;
					if (sz3[i - 1][j] >= k && sz3[i][j - 1] >= k && mp[i - k][j - k] == 'Y') ++mx;
				}
			}
			dp3[i][j] = min(mx, dp1[i - mx][j]);
			sz3[i][j] = mx;
		}
	}

	// cerr << "dp3:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << dp3[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }
	// cerr << "sz3:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << sz3[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }

	// vector<tuple<short, short, short>> sq;
	for (int i = 1; i < n; ++i) {
		for (int j = 1; j < m; ++j) {
			int mx = 0;
			if (mp[i][j] == 'B') {
				mx = 1;
				for (int k = 1; ; ++k) {
					if (k > i || k > j) break;
					if (sz4[i - 1][j] >= k && sz4[i][j - 1] >= k && mp[i - k][j - k] == 'B') ++mx;
				}
			}
			dp4[i][j] = min(mx, min(dp2[i - mx][j], dp3[i][j - mx]));
			sz4[i][j] = mx;

			at[dp4[i][j] * 2].emplace_back(i - dp4[i][j] * 2 + 1, j - dp4[i][j] * 2 + 1);
			// sq.emplace_back(i - dp4[i][j] * 2 + 1, j - dp4[i][j] * 2 + 1, dp4[i][j]);
			// cerr << i - dp4[i][j] * 2 + 1 << ' ' << j - dp4[i][j] * 2 + 1 << ' ' << dp4[i][j] << endl;
		}
	}

	// cerr << "dp4:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << dp4[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }
	// cerr << "sz4:" << endl;
	// for (int i = 0; i < n; ++i) {
	// 	for (int j = 0; j < m; ++j) {
	// 		cerr << sz4[i][j] << ' ';
	// 	}
	// 	cerr << '\n';
	// }

	vector<tuple<short, short, short, short>> qr;
	for (int i = 0; i < q; ++i) {
		int x1, x2, y1, y2; cin >> x1 >> y1 >> x2 >> y2;
		qr.emplace_back(x1, y1, x2, y2);
	}

	for (int i = 2; i <= 500; i += 2) {
		memset(pre, 0, sizeof(pre));
		for (auto &p : at[i]) {
			++pre[p.first + 1][p.second + 1];
		}
		for (int x = 1; x <= n; ++x) for (int y = 1; y <= m; ++y) pre[x][y] = pre[x][y] + pre[x - 1][y] + pre[x][y - 1] - pre[x - 1][y - 1];
		for (int j = 0; j < q; ++j) {
			auto [x1, y1, x2, y2] = qr[j];
			if (x2 - x1 + 1 < i || y2 - y1 + 1 < i) continue;
			x2 -= (i - 1), y2 -= (i - 1);
			if (pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1]) ans[j] = i * i;
		}
	}
	
	for (int i = 0; i < q; ++i) cout << ans[i] << '\n';
}
