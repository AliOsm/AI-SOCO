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

    int n, m;
    cin >> n >> m;
    vi a(n);
    vi freq(m + 1, 0);
    for (auto& x : a) {
        cin >> x;
        if (x <= m)
            ++freq[x];
    }

    for (int i = m; i > 0; --i) {
        for (int j = i + i; j <= m; j += i) {
            freq[j] += freq[i];
        }
    }

    int best = 1;
    for (int i = 0; i <= m; ++i) {
        if (freq[i] > freq[best])
            best = i;
    }

    vi ans;
    int actual_lcm = 1;
    for (int i = 0; i < n; ++i) {
        if (best % a[i] == 0) {
            ans.push_back(i + 1);
            actual_lcm /= gcd(actual_lcm, a[i]);
            actual_lcm *= a[i];
        }
    }

    cout << actual_lcm << ' ' << ans.size() << '\n';
    for (int x : ans) {
        cout << x << ' ';
    }

    return 0;
}
