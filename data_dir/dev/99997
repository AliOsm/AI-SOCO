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

int n, k;
int a[100005];
int b[100005];
int m[300];
int l[300];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %d %d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf(" %d", &a[i]);
    }

    memset(m, -1, sizeof(m));
    memset(l, 0, sizeof(l));

    for (int i = 0; i < n; ++i) {
        int v = a[i];
        if (m[v] == -1) {
            // printf("Scanning backwards for thing %d\n", v);
            int j = v;
            for (int kk = 0; kk <= min(v, k - 1); ++kk) {
                if (m[v - kk] == -1) {
                    j = v - kk;
                } else {
                    break;
                }
            }

            // can you extend the last thing to cover this?
            if (j and m[j - 1] != -1 and l[j - 1] + (v - j + 1) <= k) {
                for (; j <= v; ++j) {
                    l[j] = l[j - 1] + 1;
                    m[j] = m[j - 1];
                }
            } else {
                int src = j;
                m[src] = src;
                l[src] = 1;
                // printf("Painting up from %d\n", src);
                for (int kk = src + 1; kk <= v; ++kk) {
                    m[kk] = m[kk - 1];
                    l[kk] = l[kk - 1] + 1;
                }
            }
        }

        b[i] = m[v];
    }

    for (int i = 0; i < n; ++i) {
        printf("%d%c", b[i], " \n"[i == n - 1]);
    }
    
    return 0;
}
