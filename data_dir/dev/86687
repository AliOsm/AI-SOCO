#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <numeric>
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

constexpr int MAXN = 19;
int n;
ld a[MAXN][MAXN];

// starting with mask, probability fish i survives
ld dp[1 << MAXN][MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%Lf", &a[i][j]);
        }
    }

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            dp[mask][i] = (mask == (1 << i)) ? 1.0L : 0.0L;
        }

        int ct = __builtin_popcount(mask);
        int fights = ct * (ct - 1) / 2;
        if (fights == 0)
            continue;

        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) == 0)
                continue;
            for (int j = i + 1; j < n; ++j) {
                if ((mask & (1 << j)) == 0) {
                    continue;
                }

                for (int k = 0; k < n; ++k) {
                    dp[mask][k] += a[i][j] * dp[mask ^ (1 << j)][k] / fights;
                    dp[mask][k] += a[j][i] * dp[mask ^ (1 << i)][k] / fights;
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        printf("%.8Lf ", dp[(1 << n) - 1][i]);
    }

    return 0;
}
