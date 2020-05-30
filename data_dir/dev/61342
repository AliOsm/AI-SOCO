#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr int MAXN = 33;
constexpr int MAXK = 55;
constexpr ll INF = 1e18 + 7;

ll dp[MAXN][MAXN][MAXK];

ll solve(int n, int m, int k) {
    if (n < m) return solve(m, n, k);

    if (k == 0) return 0;
    if (n * m < k) return INF;
    if (n * m == k) {
        return 0;
    }
    ll& res = dp[n][m][k];
    if (res != -1) {
        return res;
    }

    res = INF;
    for (int left = 1; left < m; ++left) {
        int right = m - left;
        ll cost = n * n;
        for (int div = 0; div <= k; ++div) {
            res = min(res, cost + solve(n, left, div) + solve(n, right, k - div));
        }
    }

    for (int top = 1; top < n; ++top) {
        int bot = n - top;
        ll cost = m * m;
        for (int div = 0; div <= k; ++div) {
            res = min(res, cost + solve(top, m, div) + solve(bot, m, k - div));
        }
    }

    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    memset(dp, -1, sizeof(dp));

    int T;
    cin >> T;
    while (T-- > 0) {
        int n, m, k;
        cin >> n >> m >> k;

        cout << solve(n, m, k) << '\n';
    }
    
    return 0;
}
