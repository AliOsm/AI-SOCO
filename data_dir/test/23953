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

    int n, m, a, x;
    scanf(" %d", &n);
    map<int, int> price;
    for (int i = 0; i < n; ++i) {
        scanf(" %d %d", &a, &x);
        price[a] = max(price[a], x);
    }
    
    scanf(" %d", &m);
    for (int i = 0; i < m; ++i) {
        scanf(" %d %d", &a, &x);
        price[a] = max(price[a], x);
    }

    ll ans = 0LL;
    for (auto it : price) {
        ans += it.second;
    }

    printf("%lld\n", ans);
    
    return 0;
}
