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

    string s;
    cin >> s;
    int k;
    cin >> k;
    while (k-- > 0) {
        s.push_back('.');
    }

    int n = s.size();
    auto is_tandem = [&](int start, int len) {
        for (int i = start, j = start + len; i < start + len; ++i, ++j) {
            if (s[i] == '.')
                return true;

            if (s[j] != '.' and s[i] != s[j])
                return false;
        }

        return true;
    };

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 1; i + 2 * j <= n; ++j) {
            if (is_tandem(i, j)) {
                ans = max(ans, j << 1);
            }
        }
    }

    cout << ans << '\n';

    return 0;
}
