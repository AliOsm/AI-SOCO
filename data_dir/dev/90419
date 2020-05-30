#include <cstdio>
#include <algorithm>

using namespace std;
using ll = long long;

ll n, k, M, D;

ll per_person(ll x) {
    ll buckets = n / x;
    ll pp = (buckets + k - 1) / k;

    return max(1LL, pp);
}

ll find(ll dd) {
    // find the largest x such that
    // ceil(floor(n / x) / k) <= dd
    ll lo = 1;
    ll hi = n;

    while (lo + 1 < hi) {
        ll mid = lo + ((hi - lo) / 2);
        // printf("when x = %lld, we have max per person = %lld\n", mid, per_person(mid));
        if (per_person(mid) >= dd) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    return lo;
}

ll solve(ll x) {
    if (x > M) return 0;
    ll pp = per_person(x);
    if (pp > D)
        return 0;

    return x * pp;
}

int main() {
    scanf(" %lld %lld %lld %lld", &n, &k, &M, &D);
    ll ans = solve(M);
    for (ll dd = 1; dd <= D; ++dd) {
        // find an x such that per_person = dd
        // printf("For dd %lld, best x is %lld\n", dd, find(dd));
        ans = max(ans, solve(find(dd)));
    }

    printf("%lld\n", ans);

    return 0;
}
