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

constexpr int MAXN = 200005;
int n, m;
vector<int> graph[MAXN];
bool vis[MAXN];
bool iscycle;

void dfs(int u) {
    if (vis[u]) return;

    vis[u] = true;
    if (graph[u].size() != 2)
        iscycle = false;
    for (int v : graph[u]) {
        dfs(v);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %d %d", &n, &m);
    int u, v;
    for (int i = 0; i < m; ++i) {
        scanf(" %d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (!vis[i]) {
            iscycle = true;
            dfs(i);
            if (iscycle)
                ++ans;
        }
    }

    printf("%d\n", ans);
    return 0;
}
