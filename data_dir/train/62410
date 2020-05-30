#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int tc;
    cin >> tc;
    while (tc--) {
        int x, y;
        cin >> x >> y;
        int a, b;
        cin >> a >> b;
        int more = max(x, y) - min(x, y);
        long long res = 1LL * more * a;
        res += 1LL * min(x, y) * min(2 * a, b);
        cout << res << "\n";
    }
    return 0;
}

