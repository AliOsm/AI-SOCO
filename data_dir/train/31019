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

constexpr int MAXN = 300005;
int n;
int a[MAXN];
int b[MAXN];
int trie[31 * MAXN][2];
int occ[31 * MAXN];
int nnode = 1;

void insert(int node, int x, int b = 30) {
    ++occ[node];
    if (b == -1) {
        return;
    }

    int branch = (x & (1 << b)) > 0;
    if (!trie[node][branch]) {
        trie[node][branch] = nnode++;
    }

    insert(trie[node][branch], x, b - 1);
}

void remove(int node, int x, int b = 30) {
    --occ[node];
    if (b == -1)
        return;

    int branch = (x & (1 << b)) > 0;
    assert(trie[node][branch] > 0);
    remove(trie[node][branch], x, b - 1);
    if (occ[trie[node][branch]] == 0)
        trie[node][branch] = 0;
}

int query(int node, int x, int b = 30, int res = 0) {
    if (b == -1)
        return res;
    int branch = (x & (1 << b)) > 0;
    if (trie[node][branch]) {
        return query(trie[node][branch], x, b - 1, res | (branch << b));
    } else {
        return query(trie[node][1 - branch], x, b - 1, res | ((1 - branch) << b));
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; ++i) {
        scanf("%d", &b[i]);
        insert(0, b[i]);
    }

    for (int i = 0; i < n; ++i) {
        int res = query(0, a[i]);
        remove(0, res);
        // printf("a[i]: %d res %d\n", a[i], res);
        printf("%d ", res ^ a[i]);
    }

    return 0;
}
