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
int n;
char s[MAXN];
int a[MAXN];
int dp[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %s", s);
    n = strlen(s);
    a[0] = 0;
    for (int i = 1; i <= n; ++i) {
        a[i] = (s[i - 1] - '0') % 3;
    }

    for (int i = 1; i <= n; ++i) {
        int sum = a[i];
        for (int j = i; j > 0 and i - j <= 5; --j) {
            dp[i] = max(dp[i], dp[j - 1] + (sum == 0));
            sum += a[j - 1];
            sum %= 3;
        }
    }

    printf("%d\n", dp[n]);

    return 0;
}
