#include <bits/stdc++.h>
using namespace std;

int open[400005];
int dp[400005][2][2];

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin >> t; while (t--) {
		int h, n; cin >> h >> n;
		vector<int> p(n + 5, 0);
		for (int i = 1; i <= n; ++i) cin >> p[i];
		int now = 5;
		open[0] = open[1] = open[2] = open[3] = open[4] = open[5] = 1;
		for (int i = n; i >= 1; --i) {
			if (p[i] - p[i + 1] == 1) {
				++now;
				open[now] = 1;
			} else {
				++now;
				open[now] = 0;
				++now;
				open[now] = 1;
			}
		}
		n = now;
		for (int i = 0; i <= n; ++i) dp[i][0][0] = dp[i][0][1] = dp[i][1][0] = dp[i][1][1] = 100000000;
		dp[n][open[n - 1]][open[n - 2]] = 0;
		for (int i = n; i >= 4; --i) {
			for (int j = 0; j < 2; ++j) {
				for (int k = 0; k < 2; ++k) {
					if (j == 0) {
						dp[i - 1][k][open[i - 3]] = min(dp[i - 1][k][open[i - 3]], dp[i][j][k]);
					}
					if (j == 1 && k == 0) {
						dp[i - 1][k][open[i - 3]] = min(dp[i - 1][k][open[i - 3]], dp[i][j][k] + 1);
					}
					if (j == 1 && k == 1) {
						dp[i - 2][open[i - 3]][open[i - 4]] = min(dp[i - 2][open[i - 3]][open[i - 4]], dp[i][j][k]);
					}
				}
			}
		}
		cout << min(dp[4][1][1], dp[5][1][1]) << '\n';
	}
}
