#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

struct DSU {
    int n;
    // uf[x] = parent of x or negative size of component
    vector<int> uf;
    DSU(int n): n(n) {
        uf.assign(n, -1);
    }

    int find(int x) {
        return uf[x] < 0 ? x : (uf[x] = find(uf[x]));
    }

    int merge(int x, int y) {
        int xr = find(x);
        int yr = find(y);
        if (xr == yr)
            return 0;

        if (uf[yr] < uf[xr]) {
            uf[yr] += uf[xr];
            uf[xr] = yr;
        } else {
            uf[xr] += uf[yr];
            uf[yr] = xr;
        }

        return 1;
    }

    vector<vi> get_comps() {
        vector<vi> comps;

        vi comp_id(n, -1);
        for (int i = 0; i < n; ++i) {
            int root = find(i);
            if (comp_id[root] == -1) {
                comp_id[root] = comps.size();
                comps.push_back(vi());
            }

            comps[comp_id[root]].push_back(i);
        }

        return comps;
    }
};

void dfs(const vector<vi>& tree, vi& dist, int u, int p) {
    for (int v : tree[u]) {
        if (v == p) continue;
        dist[v] = dist[u] + 1;
        dfs(tree, dist, v, u);
    }
}

int solve(const vector<pii>& edges) {
    vi nodes;
    for (auto& e : edges) {
        nodes.push_back(e.first);
        nodes.push_back(e.second);
    }

    sort(all(nodes));
    nodes.erase(unique(all(nodes)), end(nodes));

    int m = nodes.size();
    DSU dsu(m);
    vector<vi> tree(m);
    for (auto& e : edges) {
        int u = lower_bound(all(nodes), e.first) - begin(nodes);
        int v = lower_bound(all(nodes), e.second) - begin(nodes);

        tree[u].push_back(v);
        tree[v].push_back(u);
        dsu.merge(u, v);
    }
    
    vector<vi> comps = dsu.get_comps();
    vi dist(m, 1);
    for (vi& comp : comps) {
        int u = comp[0];
        dfs(tree, dist, u, -1);

        int big_child = u;
        int big_dist = dist[u];

        for (int v : comp) {
            if (dist[v] > big_dist) {
                big_child = v;
                big_dist = dist[v];
            }

            dist[v] = 1;
        }

        dfs(tree, dist, big_child, -1);
    }

    return *max_element(all(dist));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    constexpr int MAXA = 200005;
    vector<vi> pf(MAXA);
    vi primes;
    for (int i = 2; i < MAXA; ++i) {
        if (pf[i].empty()) {
            primes.push_back(i);
            for (int j = i; j < MAXA; j += i) {
                pf[j].push_back(i);
            }
        }
    }

    int n;
    cin >> n;
    vi a(n);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] > 1)
            ans = 1;
    }

    vector<vector<pii>> edges(MAXA);
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        int g = gcd(a[u], a[v]);

        for (int p : pf[g]) {
            edges[p].emplace_back(u, v);
        }
    }

    for (int p : primes) {
        if (edges[p].empty())
            continue;

        ans = max(ans, solve(edges[p]));
    }

    cout << ans << '\n';

    return 0;
}
