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

// see if s[start, start + len) contains any of boring
bool works(const string& s, const vector<string>& boring, const vector<vector<int>>& occ, int start, int len) {
    for (int i = 0; i < boring.size(); ++i) {
        int bore_len = boring[i].size();
        auto it = lower_bound(begin(occ[i]), end(occ[i]), start);
        if (it == end(occ[i]))
            continue;
        if (*it + bore_len <= start + len)
            return false;
    }

    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n, m;
    string s;
    cin >> s;
    n = s.size();
    cin >> m;
    vector<string> boring(m);
    for (int i = 0; i < m; ++i) {
        cin >> boring[i];
    }
    vector<vector<int>> occ(m);
    for (int i = 0; i < m; ++i) {
        int sz = boring[i].size();
        for (int j = 0; j + sz <= n; ++j) {
            bool match = true;
            for (int k = 0; k < sz; ++k) {
                if (s[j + k] != boring[i][k]) {
                    match = false;
                    break;
                }
            }

            if (match) {
                occ[i].push_back(j);
            }
        }
    }

    int ans = 0;
    int start_pos = 0;
    for (int i = 0; i < n; ++i) {
        int lo = 0;
        int hi = n - i + 1;
        if (hi < ans)
            break;
        while (lo + 1 < hi) {
            int mid = (lo + hi) >> 1;
            if (works(s, boring, occ, i, mid)) {
                lo = mid;
            } else {
                hi = mid;
            }
        }

        if (lo > ans) {
            ans = lo;
            start_pos = i;
        }
    }

    cout << ans << ' ' << start_pos << '\n';
    
    return 0;
}
