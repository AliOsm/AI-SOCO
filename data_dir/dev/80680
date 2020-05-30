#include <cstdio>
#include <vector>

using namespace std;

const int MAXB = 17;
const int MAXN = 1 << MAXB;

vector<pair<int, int> > e[MAXN];
int v[MAXN], c[MAXN], d[MAXN], r[MAXN], p[MAXN][MAXB];

void dfs(int v, int f) {
    p[v][0] = f;
    for (int i = 1; i < MAXB; ++i) {
        p[v][i] = p[p[v][i - 1]][i - 1];
    }
    for (auto& i: e[v]) {
        if (i.first == f) {
            continue;
        }
        d[i.first] = d[v] + 1;
        r[i.first] = i.second;
        dfs(i.first, v);
    }
}

int go(int v, int d) {
    for (int i = 0; i < MAXB; ++i) {
        if (d & (1 << i)) {
            v = p[v][i];
        }
    }
    return v;
}

int lca(int i, int j) {
    if (d[i] > d[j]) {
        swap(i, j);
    }
    j = go(j, d[j] - d[i]);
    if (i == j) {
        return i;
    }
    for (int k = MAXB - 1; k >= 0; --k) {
        if (p[i][k] != p[j][k]) {
            i = p[i][k];
            j = p[j][k];
        }
    }
    return p[i][0];
}

void gao(int v, int f) {
    for (auto& i: e[v]) {
        if (i.first == f) {
            continue;
        }
        gao(i.first, v);
        c[i.second] = ::v[i.first];
        ::v[v] += ::v[i.first];
    }
}

int main() {
    int n, m, a, b;

    scanf("%d", &n);
    for (int i = 1; i < n; ++i) {
        scanf("%d%d", &a, &b);
        --a;
        --b;
        e[a].push_back({b, i});
        e[b].push_back({a, i});
    }
    d[0] = 0;
    dfs(0, 0);

    scanf("%d", &m);
    for (int i = 0; i < m; ++i) {
        scanf("%d%d", &a, &b);
        --a;
        --b;
        ++v[a];
        ++v[b];
        v[lca(a, b)] -= 2;
    }
    gao(0, 0);

    for (int i = 1; i < n; ++i) {
        printf("%d ", c[i]);
    }

    return 0;
}
