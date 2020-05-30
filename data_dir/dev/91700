#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <complex>

using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;

constexpr int MAXN = 503;
constexpr int MOD = 1e9 + 7;
int n;
int a[MAXN][MAXN];

int dp[2][MAXN][MAXN];

int sum(const int& a, const int& b) {
    int c = a + b;
    if (c >= MOD)
        c -= MOD;
    return c;
}

int prod(const int& a, const int& b) {
    return (1LL * a * b) % MOD;
}

int modpow(const int& base, const int& exp) {
    int res = 1;
    int cur = base;
    for (int p = 1; p <= exp; p <<= 1) {
        if (exp & p) res = prod(res, cur);
        cur = prod(cur, cur);
    }
    return res;
}

int solve(int has_edge, int start, int end) {
    if (start == end)
        return 0;

    if ((start + 1) % n == end)
        return 1;

    if (dp[has_edge][start][end] != -1)
        return dp[has_edge][start][end];

    // printf("%d %d %d\n", has_edge, start, end);

    int ret = 0;
    for (int mid = (start + 1) % n; mid != end; mid = (mid + 1) % n) {
        // printf("mid: %d\n", mid);
        if (a[start][mid] and !has_edge) {
            ret = sum(ret, prod(solve(0, start, mid), solve(0, mid, end)));
        }

        if (a[mid][end]) {
            ret = sum(ret, prod(solve(1, start, mid), solve(0, mid, end)));
        }
    }

    return dp[has_edge][start][end] = ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%d", &a[i][j]);
        }
    }

    memset(dp, -1, sizeof(dp));

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (a[i][j]) {
                ans = sum(ans, prod(solve(0, i, j), solve(0, j, i)));
            }
        }
    }

    ans = prod(ans, modpow(n - 1, MOD - 2));

    printf("%d\n", ans);

    return 0;
}
