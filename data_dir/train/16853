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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n, w;
    scanf(" %d %d", &n, &w);
    int min_pref = 0;
    int max_pref = 0;
    int cur = 0;
    int x;
    for (int i = 0; i < n; ++i) {
        scanf(" %d", &x);
        cur += x;
        min_pref = min(min_pref, cur);
        max_pref = max(max_pref, cur);
    }

    if (min_pref < -w or max_pref > w) {
        printf("0\n");
        return 0;
    }

    int l = -min_pref;
    int r = w - max_pref;
    // printf("l r %d %d\n", l, r);
    printf("%d\n", max(0, r - l + 1));

    return 0;
}
