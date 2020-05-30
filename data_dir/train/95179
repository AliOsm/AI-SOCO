#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;
const int MAXN = 100005;
int n;
long long a[MAXN];
long long d[2][MAXN];
// best sum starting at i
long long dp[2][MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    scanf("%d", &n);

    for (long long i = 0; i < n; ++i)
        scanf("%lld", a + i);

    for (long long i = 1; i < n; ++i) {
        d[0][i - 1] = abs(a[i] - a[i - 1]);
        d[1][i - 1] = abs(a[i] - a[i - 1]);
        if (i & 1)
            d[0][i - 1] *= -1;
        else
            d[1][i - 1] *= -1;
    }

    long long ans = 0LL;
    for (long long j = 0; j < 2; ++j) {
        dp[j][n - 1] = d[j][n - 1];
        for (long long i = n - 2; i >= 0; --i) {
            dp[j][i] = d[j][i] + max(dp[j][i + 1], 0LL);
            if (d[j][i] > 0LL)
                ans = max(ans, dp[j][i]);
        }
    }

    /*
    for (int j = 0; j < 2; ++j) {
        for (int i = 0; i < n - 1; ++i)
            printf("%lld ", d[j][i]);
        printf("\n");

    }
        printf("\n");
    for (int j = 0; j < 2; ++j) {
        for (int i = 0; i < n - 1; ++i)
            printf("%lld ", dp[j][i]);
        printf("\n");

    }
    */

    printf("%lld\n", ans);
    return 0;
}
