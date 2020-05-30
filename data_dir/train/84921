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
    vi a(n);
    vi b(n + 1);
    b[0] = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        b[i + 1] = a[i] ^ b[i];
    }

    if (b[n] == 0) {
        cout << "-1\n";
        return 0;
    }

    // max ans is 30
    // try each ans
    int ans = 1;
    for (int k = 30; k >= 0; --k) {
        int idx = -1;
        for (int i = ans; i <= n; ++i) {
            if (b[i] & (1 << k)) {
                idx = i;
                break;
            }
        }

        if (idx == -1) continue;

        swap(b[idx], b[ans]);
        for (int i = ans + 1; i <= n; ++i) {
            if (b[i] & (1 << k)) {
                b[i] ^= b[ans];
            }
        }
        ++ans;
    }

    // 0 5 0 2 0
    
    cout << (ans - 1) << '\n';
    return 0;
}
