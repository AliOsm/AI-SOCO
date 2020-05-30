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

constexpr int MAXN = 5003;
int n;
int q[2][MAXN];
int f[MAXN][MAXN];

int p[MAXN], b[MAXN], ans[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        printf("? %d %d\n", i, 0);
        fflush(stdout);
        scanf("%d", &q[0][i]);
    }

    for (int j = 0; j < n; ++j) {
        printf("? %d %d\n", 0, j);
        fflush(stdout);
        scanf("%d", &q[1][j]);
    }

    // Now we can answer any query as f(i, j) = q[0][i] ^ q[1][j] ^ q[0][0];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            f[i][j] = q[0][i] ^ q[1][j] ^ q[0][0];
            // printf("%d ", f[i][j]);
        }
        // printf("\n");
    }


    // Now to actually solve the problem...
    // there has to be a 0 
    // so that means the answer is a row or column in the matrix
    int total = 0;
    ans[0] = -1;
    for (int j = 0; j < n; ++j) {
        // assume that b[j] = 0
        for (int i = 0; i < n; ++i) {
            p[i] = f[i][j];
            b[f[i][j]] = i;
        }

        int row = b[0];
        bool valid = true;

        for (int i = 0; i < n; ++i) {
            if (f[row][i] != b[i]) {
                valid = false;
                break;
            }
        }

        if (valid) {
            ++total;
            if (ans[0] == -1) {
                for (int i = 0; i < n;++i) {
                    ans[i] = p[i];
                }
            }
        }
    }

    printf("%c\n", '!');
    printf("%d\n", total);
    for (int i = 0; i < n; ++i) {
        printf("%d%c", ans[i], i != n - 1 ? ' ' : '\n');
    }
    fflush(stdout);

    return 0;
}
