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

constexpr int MAXN = 100005;
int n;
ll a[MAXN], b[MAXN];
ll pb[MAXN]; 
ll freqa[MAXN];
ll extra[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        scanf("%lld", &a[i]);
    }
    for (int i = 1; i <= n; ++i) {
        scanf("%lld", &b[i]);
        pb[i] = pb[i - 1] + b[i];
    }

    for (int i = 1; i <= n; ++i) {
        if (b[i] >= a[i]) {
            // fully melts on first day
            extra[i] += a[i];
        } else if (pb[n] - pb[i - 1] <= a[i]) {
            // Doesn't melt at all 
            ++freqa[i];
        } else {
            int lo = i;
            int hi = n;
            while (lo + 1 < hi) {
                int mid = (lo + hi) >> 1;
                if (pb[mid] - pb[i - 1] <= a[i]) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }

            ++freqa[i];
            --freqa[hi];
            extra[hi] += a[i] - pb[lo] + pb[i - 1];
        }
    }

    for (int i = 1; i <= n; ++i) {
        freqa[i] += freqa[i - 1];
        ll cur = freqa[i] * b[i] + extra[i];

        printf("%lld ", cur);
    }
    printf("\n");

    return 0;
}
