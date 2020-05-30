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
    vi vis(n, 0);
    vector<vi> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    set<int> s;
    for (int x : graph[0])
        s.insert(x);

    vi ans;
    ans.push_back(0);
    vis[0] = true;

    while (ans.size() < n) {
        while (vis[*begin(s)]) {
            s.erase(begin(s));
        }

        int u = *begin(s);
        ans.push_back(u);
        vis[u] = true;
        for (int v : graph[u]) {
            if (!vis[v]) {
                s.insert(v);
            }
        }
    }

    for (int x : ans) {
        cout << (x + 1) << ' ';
    }
    
    return 0;
}
