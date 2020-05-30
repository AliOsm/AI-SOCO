#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vl = vector<ll>;

vector<pll> factor(ll n) {
    vector<pll> factors;
    ll two = 0;
    while (!(n & 1)) {
        ++two;
        n >>= 1;
    }
    if (two)
        factors.emplace_back(2LL, two);

    for (ll p = 3; p * p <= n; p += 2) {
        ll occ = 0;
        while (n % p == 0) {
            ++occ;
            n /= p;
        }

        if (occ) {
            factors.emplace_back(p, occ);
        }
    }

    if (n > 1) {
        factors.emplace_back(n, 1);
    }

    return factors;
}

constexpr int MOD = 1000000007;

inline ll sum(ll a, ll b) {
    return (a + b) % MOD;
}

inline ll prod(ll a, ll b) {
    return (1LL * a * b) % MOD;
}

ll modpow(ll base, ll exp) {
    if (!exp) return 1;
    if (exp & 1) return prod(base, modpow(base, exp - 1));
    return modpow(prod(base, base), exp >> 1);
}

inline ll inv(ll x) {
    return modpow(x, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    ll n;
    ll k;
    cin >> n >> k;
    vector<pll> pf = factor(n);

    ll ans = 1;
    for (auto& e : pf) {
        ll p = e.first;
        ll occ = e.second;
        vl invs(occ + 1, 0);
        for (int i = 0; i <= occ; ++i) {
            invs[i] = inv(i + 1);
        }

        vector<vl> dp(k + 1, vl(occ + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= occ; ++i) {
            dp[0][i] = prod(dp[0][i - 1], p);
        }
        for (int i = 1; i <= k; ++i) {
            // compute prefix sums of the prior row
            for (int j = 1; j <= occ; ++j) {
                dp[i - 1][j] = sum(dp[i - 1][j - 1], dp[i - 1][j]);
            }

            dp[i][0] = 1;
            for (int j = 1; j <= occ; ++j) {
                dp[i][j] = prod(invs[j], dp[i - 1][j]);
            }
        }

        ans = prod(ans, dp[k][occ]);
    }

    cout << ans << '\n';

    return 0;
}
