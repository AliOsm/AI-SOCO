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
int n, m, q;
int uf[MAXN];

int find(int x) {
    return uf[x] = x == uf[x] ? x : find(uf[x]);
}

int merge(int x, int y) {
    int xr = find(x);
    int yr = find(y);
    if (xr == yr)
        return 0;
    uf[xr] = yr;
    return 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %d %d %d", &n, &m, &q);
    map<int, vector<int>> by_x;
    map<int, vector<int>> by_y;

    int x, y;
    for (int i = 0; i < q; ++i) {
        scanf(" %d %d", &x, &y);
        by_x[x].push_back(i);
        by_y[y].push_back(i);

        uf[i] = i;
    }

    int blocks = q;
    for (auto it : by_x) {
        for (int i = 1; i < it.second.size(); ++i) {
            blocks -= merge(it.second[i - 1], it.second[i]);
        }
    }
    
    for (auto it : by_y) {
        for (int i = 1; i < it.second.size(); ++i) {
            blocks -= merge(it.second[i - 1], it.second[i]);
        }
    }

    int ans = n + m - static_cast<int>(by_x.size()) - static_cast<int>(by_y.size()) + blocks - 1;
    printf("%d\n", ans);
    return 0;
}
