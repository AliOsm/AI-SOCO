#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <queue>

using namespace std;

using ll = long long;
using ld = long double;

constexpr int MAXN = 100005;
vector<int> vals[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n, k, m;
    scanf("%d %d %d", &n, &k, &m);

    int best_ind = 0;
    int x;
    for (int i = 0; i < n; ++i) {
        scanf("%d", &x);
        vals[x % m].push_back(x);
        if (vals[x % m].size() > vals[best_ind].size()) {
            best_ind = x % m;
        }
    }

    if (vals[best_ind].size() < k) {
        printf("%s\n", "No");
        return 0;
    }

    printf("%s\n", "Yes");
    for (int i = 0; i < k; ++i) {
        printf("%d%c", vals[best_ind][i], i == k - 1 ? '\n' : ' ');
    }
    
    return 0;
}
