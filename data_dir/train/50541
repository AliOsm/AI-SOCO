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

    ll x, y, z;
    cin >> x >> y >> z;

    ll ans = (x + y) / z;
    ll cost = 0;
    if (ans > (x / z) + (y / z)) {
        ll p = x % z;
        ll q = y % z;

        cost = min(min(p, q), min(z - p, z - q));
    }

    cout << ans << ' ' << cost << '\n';
    
    return 0;
}
