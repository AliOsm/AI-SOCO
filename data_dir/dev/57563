#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <tuple>

using namespace std;

const int MAXK = 1003;
const int MAXD = 16004;
const double EPS = 1e-7;

int k;
// dp[i][j] = prob of success when you need i new ones with j days remaining
double prev_dp[MAXD];
double dp[MAXD];

int main() {
    ios_base::sync_with_stdio(false);
    int q;
    scanf("%d %d", &k, &q);

    for (int i = 0; i < MAXD; ++i) {
        prev_dp[i] = 1.0;
        dp[i] = 0.0;
    }

    for (int i = 1; i <= k; ++i) {
        dp[i - 1] = 0.0;
        for (int j = i; j < MAXD; ++j) {
            dp[j] = ((k - i) * dp[j - 1] + i * prev_dp[j - 1]) / k;
        }

        memcpy(prev_dp, dp, sizeof(dp));
    }

    /*
    for (int i = 0; i < 10; ++i) {
        printf("%.3f ", prev_dp[i]);
    }
    puts("");
    */

    int p;
    while (q-- > 0) {
        int lo = 0;
        int hi = MAXD - 1;

        scanf("%d", &p);
        double target = (p - EPS) / 2000.0;
        // printf("Hitting %.3f\n", target);

        while (lo + 1 < hi) {
            int mid = (lo + hi) / 2;
            double it = prev_dp[mid];
            // printf("%d %.3f\n", mid, it);
            if (it >= target) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        printf("%d\n", hi);
    }

    return 0;
}
