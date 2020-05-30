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

ll gcd(ll a, ll b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    ll n, a, b;
    scanf(" %lld %lld %lld", &n, &a, &b);

    ll g = gcd(a, b);
    if (n % g != 0) {
        printf("NO\n");
        return 0;
    }

    bool ss = false;
    if (a < b) {
        swap(a, b);
        ss = true;
    }

    a /= g;
    b /= g;
    n /= g;

    for (ll x = 0; a * x <= n; ++x) {
        ll y = (n - x * a) / b;
        if (y >= 0 and x * a + y * b == n) {
            printf("YES\n");
            if (ss)
                printf("%lld %lld\n", y, x);
            else
                printf("%lld %lld\n", x, y);
            return 0;
        }
    }

    printf("NO\n");
    return 0;
}
