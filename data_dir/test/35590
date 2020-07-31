#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    cin >> tt;
    while (tt--) {
        int n, m;
        cin >> n >> m;
        int blk = (n - m) / (m + 1);
        int rem = (n - m) % (m + 1);
        auto get = [&](int x) {
            return (1LL * x * (x + 1)) / 2;
        };
        long long ans = rem * get(blk + 1) + (m + 1 - rem) * get(blk);
        ans = -ans + get(n);
        cout << ans << "\n";
    }
    return 0;
}

