#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <complex>

using namespace std;

const int MAXN = 100005;
int n, c, d;

vector<pair<int, int> > coins;
vector<pair<int, int> > diam;

int m[2][MAXN];

char opcode[4];

int bs(vector<pair<int, int> >& data, int total, int cap) {
    if (data.empty() or data[0].first > total) return -1;
    if (data[cap - 1].first <= total) return cap - 1;

    int lo = 0;
    int hi = cap - 1;
    while (lo + 1 < hi) {
        int mid = (lo + hi) / 2;
        if (data[mid].first <= total) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    if (data[lo].first <= total) {
        return lo;
    } else {
        return -1;
    }
}

int solve(vector<pair<int, int> >& data, int total, int v) {
    int n = data.size();
    if (n < 2 or data[0].first + data[1].first > total)
        return 0;

    int ans = 0;
    for (int i = 1; i < n; ++i) {
        int left = total - data[i].first;
        int ind = bs(data, left, i);

        if (ind >= 0) {
            /*
            if (data[i].second + m[v][ind] > ans) {
                printf("%d %d\n", i, ind);
            }
            */
            ans = max(ans, data[i].second + m[v][ind]);
        }
    }

    // printf("%d: %d\n", v, ans);
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);

    scanf("%d %d %d", &n, &c, &d);
    int b, p;
    for (int i = 0; i < n; ++i) {
        scanf("%d %d %s", &b, &p, opcode);
        if (opcode[0] == 'C')
            coins.push_back(make_pair(p, b));
        else
            diam.push_back(make_pair(p, b));
    }

    sort(coins.begin(), coins.end());
    sort(diam.begin(), diam.end());
    if (!coins.empty()) {
        m[0][0] = coins[0].second;
        for (int i = 1; i < coins.size(); ++i) {
            m[0][i] = max(m[0][i - 1], coins[i].second);
        }
    }

    if (!diam.empty()) {
        m[1][0] = diam[0].second;
        for (int i = 1; i < diam.size(); ++i) {
            m[1][i] = max(m[1][i - 1], diam[i].second);
        }
    }

    /*
    printf("Coins\n");
    for (int i = 0; i < coins.size(); ++i) {
        printf("%d %d\n", coins[i].first, coins[i].second);
    }
    for (int i = 0; i < coins.size(); ++i) {
        printf("%d%c", m[0][i], i == coins.size() - 1 ? '\n' : ' ');
    }
    printf("Diamonds\n");
    for (int i = 0; i < diam.size(); ++i) {
        printf("%d %d\n", diam[i].first, diam[i].second);
    }
    for (int i = 0; i < diam.size(); ++i) {
        printf("%d%c", m[1][i], i == diam.size() - 1 ? '\n' : ' ');
    }
    */

    int ans = 0;

    ans = max(ans, solve(coins, c, 0));
    ans = max(ans, solve(diam, d, 1));
    
    int cind = bs(coins, c, coins.size());
    int dind = bs(diam, d, diam.size());

    // printf("cind: %d dind: %d\n", cind, dind);
    if (cind >= 0 and dind >= 0 and coins[cind].first <= c and diam[dind].first <= d) {
        ans = max(ans, m[0][cind] + m[1][dind]);
    }

    printf("%d\n", ans);
    return 0;
}
