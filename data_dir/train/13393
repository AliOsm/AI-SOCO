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

constexpr int MAXN = 1e6 + 6;
constexpr ll INF = 1e18;
int n, m, k;
// last[i] = j where j <= i and j is unblocked
int last[MAXN];
int a[MAXN];

int score(int len) {
    int p = 0;
    int hops = 0;
    while (p < n) {
        p = p + len;
        ++hops;
        if (p >= n) return hops;
        p = last[p];
    }

    return hops;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %d %d %d", &n, &m, &k);
    for (int i = 0; i <= n; ++i) {
        last[i] = i;
    }

    int x;
    int max_seg = 0;
    for (int i = 0; i < m; ++i) {
        scanf(" %d", &x);
        if (x == 0) {
            printf("-1\n");
            return 0;
        }

        last[x] = last[x - 1];
        max_seg = max(max_seg, x - last[x]);
    }

    if (max_seg >= k) {
        printf("-1\n");
        return 0;
    }

    for (int i = 1; i <= k; ++i) {
        scanf(" %d", &a[i]);
    }

    ll ans = INF;
    for (int i = max_seg + 1; i <= k; ++i) {
        int hops = score(i);
        ans = min(ans, 1LL * a[i] * hops);
    }

    printf("%lld\n", ans);

    return 0;
}
