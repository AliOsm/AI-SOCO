#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

/*
 * 1 4 => 1
 * 1 1 4 => 2
 * 3 2 2 2 => 3
 * 3 2 2 => 2
 *
 * if you have a 1, must use it as a small
 * otherwise, greedily use up smalls?
 */
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;

    vector<ll> a(n);
    ll ans = 0LL;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    ll dubs = 0;
    for (int i = n - 1; i >= 0; --i) {
        dubs += a[i] / 2;
        if (a[i] % 2 == 1) {
            if (dubs) {
                --dubs;
                ++ans;
            }
        }
    }

    ans += 2LL * (dubs / 3LL);
    dubs %= 3LL;
    if (dubs == 2) {
        ++ans;
    }

    cout << ans << '\n';
    
    return 0;
}
