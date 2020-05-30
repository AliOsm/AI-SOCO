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
    vector<pii> up, down;
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        if (x < y) {
            up.emplace_back(-y, i);
        } else {
            down.emplace_back(x, i);
        }
    }

    auto& ans = up.size() > down.size() ? up : down;
    sort(all(ans));
    cout << ans.size() << '\n';
    for (auto& p : ans) {
        cout << (p.second + 1) << ' ';
    }

    return 0;
}
