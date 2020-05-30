#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <complex>

using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using pil = pair<int, long long>;

constexpr int MAXN = 200005;
int n, m;
vector<pil> graph[MAXN];;
ll cost[MAXN];
ll dist[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d %d", &n, &m);
    int u, v;
    ll w;
    for (int i = 0; i < m; ++i) {
        scanf("%d %d %lld", &u, &v, &w);
        graph[u].push_back({v, 2LL * w});
        graph[v].push_back({u, 2LL * w});
    }

    for (int u = 1; u <= n; ++u) {
        scanf("%lld", cost + u);
    }

    priority_queue<pair<ll, int>, vector<pair<ll, int> >, greater<pair<ll, int> > > pq;
    for (int u = 1; u <= n; ++u) {
        dist[u] = cost[u];
        pq.push({dist[u], u});
    }

    ll d;
    while (!pq.empty()) {
        tie(d, u) = pq.top();
        pq.pop();

        if (d > dist[u])
            continue;

        for (auto& e : graph[u]) {
            tie(v, w) = e;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        printf("%lld%c", dist[i], " \n"[i == n]);
    }

    return 0;
}
