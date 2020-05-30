#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;
    vector<pair<ll, ll>> a(n);
    ll tot = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first >> a[i].second;
        tot += a[i].first;
    }
    if (tot < 0) {
        for (int i = 0; i < n; ++i) {
            a[i].first *= -1;
        }
    }

    ll s = 0;
    for (ll k = 62; k >= 0; --k) {
        ll bit_sum = 0;
        for (int i = 0; i < n; ++i) {
            ll val = a[i].first;
            ll mask = a[i].second;
            if ((mask & (-mask)) == (1LL << k)) {
                bit_sum += val;
            }
        }

        if (bit_sum > 0) {
            s |= (1LL << k);
            for (int i = 0; i < n; ++i) {
                ll mask = a[i].second;
                if (mask & (1LL << k)) {
                    a[i].first *= -1;
                }
            }
        }
    }

    cout << s << '\n';

    return 0;
}
