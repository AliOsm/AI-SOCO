#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;
using vl = vector<ll>;

void dfs(const vector<vi>& tree, vl& s, vi& h, int u, int p = -1) {
    if (p >= 0 and s[u] == -1) {
        s[u] = s[p];
    }

    for (int v : tree[u]) {
        h[v] = h[u] + 1;
        dfs(tree, s, h, v, u);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;
    vi p(n);
    vector<vi> tree(n);
    for (int i = 1; i < n; ++i) {
        cin >> p[i];
        --p[i];
        tree[p[i]].push_back(i);
    }

    vl s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
    vi h(n, 0);
    dfs(tree, s, h, 0);

    bool poss = true;
    vl a(n, -1);
    a[0] = s[0];
    for (int i = 1; i < n; ++i) {
        a[i] = s[i] - s[p[i]];
        if (a[i] < 0) {
            poss = false;
        }
    }

    /*
    for (int x : s) {
        cout << x << ' ';
    }
    cout << '\n';
    for (int x : a) {
        cout << x << ' ';
    }
    cout << '\n';
    */

    ll ans = a[0];
    for (int i = 1; i < n; ++i) {
        if (h[i] & 1 and !tree[i].empty()) {
            ll min_a = 1e17;
            for (int v : tree[i]) {
                min_a = min(min_a, a[v]);
            }
            a[i] += min_a;
            for (int v : tree[i]) {
                a[v] -= min_a;
            }
        }

        ans += a[i];
    }

    /*
    for (int x : s) {
        cout << x << ' ';
    }
    cout << '\n';
    for (int x : a) {
        cout << x << ' ';
    }
    cout << '\n';
    */

    if (poss) {
        cout << ans << '\n';
    } else {
        cout << -1 << '\n';
    }

    // impossible if s decreases somehow
    // otherwise s should always increase from the root
    // just greedily set it to its parent
    // if this causes a contradiction, impossible

    return 0;
}
