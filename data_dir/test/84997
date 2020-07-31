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

ll solve(ll n, ll x, ll y) {
    ll half = (1LL * n * n  +1LL) / 2LL;
    if (x == n - 1 and y == n - 1) {
        return half;
    }

    ll p = 1LL * n * x + y;
    ll ans = 0LL;
    if (n & 1) {
        if (p % 2LL == 1LL) {
            ans += half;
            --p;
        }
    } else {
        if ((x + y) % 2 == 1) {
            ans += half;
        }
    }

    ans += (p / 2LL);
    return ans + 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    ll n; int q;
    scanf(" %lld %d", &n, &q);
    ll x, y;
    while (q-- > 0) {
        scanf(" %lld %lld", &x, &y);
        --x;
        --y;
        printf("%lld\n", solve(n, x, y));
    }
    
    return 0;
}
