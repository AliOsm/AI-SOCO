#include <bits/stdc++.h>

using namespace std;

typedef long long int LL;

const int MAXN = 1e7 + 100;

LL dp[MAXN];

int main() {
	LL n, x, y;
	cin >> n >> x >> y;
	for (int i = 0; i < MAXN; i++)
		dp[i] = 1LL * i * x;
	
	int cnt = 10;
	while (cnt--) {
		for (int i = 1; i < MAXN; i++) {
			if (2 * i < MAXN)
				dp[2 * i] = min(dp[2 * i], dp[i] + y);
			if (i + 1 < MAXN)
				dp[i + 1] = min(dp[i + 1], dp[i] + x);
			if (i - 1 >= 0)
				dp[i - 1] = min(dp[i - 1], dp[i] + x);
		}
	}
	cout << dp[n] << endl;
	return 0;
}
