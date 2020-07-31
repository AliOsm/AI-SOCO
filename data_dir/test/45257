#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

void dfs(const vector<vi>& tree, vi& dist, int u) {
    for (int v : tree[u]) {
        if (dist[v] == -1) {
            dist[v] = dist[u] + 1;
            dfs(tree, dist, v);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    /*
     * Create 2 chains, one of length h, one of length d - h
     * then compute the diameter i guess
     *
     * handle h = d = n - 1 ?
     */

    int n, d, h;
    cin >> n >> d >> h;
    if (d > 2 * h) {
        cout << "-1";
        return 0;
    }
    assert(h <= d);

    // h <= d <= 2 * h
    vi p(n);

    for (int i = 1; i <= h; ++i) {
        p[i] = i - 1;
    }

    // h is 3
    // d is 5
    // 0 - 1 - 2 - 3
    //   \ 4 - 5
    if (h < d) {
        p[h + 1] = 0;
        for (int i = h + 2; i <= d; ++i) {
            p[i] = i - 1;
        }
    }

    for (int i = d + 1; i < n; ++i) {
        p[i] = h == d;
    }

    vector<vi> tree(n);
    for (int i = 1; i < n; ++i) {
        assert(p[i] < i);
        tree[p[i]].push_back(i);
        tree[i].push_back(p[i]);
    }

    vi dist(n, -1);
    dist[0] = 0;
    dfs(tree, dist, 0);
    int far = 0;

    for (int i = 0; i < n; ++i) {
        if (dist[i] > dist[far]) {
            far = i;
        }
    }

    if (dist[far] > h) {
        cout << "-1\n";
        return 0;
    }

    dist.assign(n, -1);
    dist[far] = 0;
    dfs(tree, dist, far);

    int diam = 0;
    for (int i = 0; i < n; ++i) {
        diam = max(diam, dist[i]);
    }

    if (diam != d) {
        cout << "-1\n";
        return 0;
    }

    for (int i = 1; i < n; ++i) {
        assert(p[i] != i);
        cout << (p[i] + 1) << ' ' << (i + 1) << '\n';
    }
    
    return 0;
}
