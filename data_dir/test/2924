#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>

using namespace std;

constexpr int MAXN = 100005;
int n;
vector<int> tree[MAXN];
int sz[MAXN];
double ans[MAXN];

void dfs1(int u) {
    sz[u] = 1;
    for (int v : tree[u]) {
        dfs1(v);
        sz[u] += sz[v];
    }
}

void dfs2(int u, double t) {
    ans[u] = t;
    for (int v : tree[u]) {
        dfs2(v, t + 1.0 + (sz[u] - sz[v] - 1.0) / 2.0);
    }
}

int main() {
    scanf("%d", &n);
    int x;
    for (int i = 2; i <= n; ++i) {
        scanf("%d", &x);
        tree[x].push_back(i);
    }

    dfs1(1);
    dfs2(1, 1.0);

    for (int i = 1; i <= n; ++i) {
        printf("%lf ", ans[i]);
    }
    printf("\n");

    return 0;
}
