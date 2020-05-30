#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

ll solve(ll n, ll m) {
    ll vals = n / m;
    vector<ll> v(10);
    // 0 7 4 1 8 5 2 9 6 3
    for (int i = 0; i < 10; ++i) {
        v[i] = i * m % 10;
    }

    ll tot = 0;
    for (ll x : v)
        tot += x;

    ll ans = tot * (vals / 10);
    for (int i = 0; i <= (vals % 10); ++i) {
        ans += v[i];
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int T;
    cin >> T;
    while (T-- > 0) {
        ll n, m;
        cin >> n >> m;
        cout << solve(n, m) << '\n';
    }
    
    return 0;
}
