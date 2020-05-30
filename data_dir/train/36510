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

constexpr int MAXN = 100005;
int n;
char s[MAXN], t[MAXN];
int freq[2][2];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %d", &n);
    scanf(" %s", s);
    scanf(" %s", t);
    for (int i = 0; i < n; ++i) {
        ++freq[t[i] - '0'][s[i] - '0'];
    }

    ll ans = 0LL;
    ll ans2 = 0LL;
    for (int i = 0; i < n; ++i) {
        if (t[i] == '0') {
            // printf("%d %d\n", freq[0][1 - (s[i] - '0')], freq[1][1 - (s[i] - '0')]);
            ans += freq[1][1 - (s[i] - '0')];
            ans2 += freq[0][1 - (s[i] - '0')];
        }
    }

    // printf("ans %lld ans2 %lld\n", ans, ans2);
    printf("%lld\n", ans + ans2 / 2);

    return 0;
}
