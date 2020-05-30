#include <iostream>
#include <string>
#include <memory.h>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <fstream>
#include <queue>
#include <list>
using namespace std;
struct has{
    long long h1, h2;
    int n;
};
has h[26];
has ht[26];
has f[26];
has hs[26][300005];
vector < int > ans;
char ss[500005];
char tt[500005];
int arr[500005];
string s, t;
int n, m;
int mod1,mod2;
int sa[300005], sb[300005];
long long st1[1000005];
long long st2[1000005];
bool prost(int n) {
    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0) return false;
    return true;
}
bool cmp_h(has a, has b) {
    return (a.h1 < b.h1 || (a.h1 == b.h1 && a.h2 < b.h2));
}
int main() {
  //  freopen("input.txt","r",stdin);
  //  ios::sync_with_stdio(false);
    scanf("%d%d\n", &n, &m);
    scanf("%s", ss);
    scanf("%s", tt);
    mod1 = 500000000; mod2 = 300000000;
    while (!prost(mod1)) mod1++;
    while (!prost(mod2)) mod2++;
    for (int i = 0; i < n; ++i) {
        sa[i] = ss[i] - 'a';
    }
    st1[0] = st2[0] = 1;
    for (int i = 1; i <= 1000000; ++i) {
        st1[i] = 1LL * st1[i - 1] * 29 % mod1;
        st2[i] = 1LL * st2[i - 1] * 31 % mod2;
    }
    for (int i = 0; i < m; ++i) {
        sb[i] = tt[i] - 'a';
    }

    for (int i = 0; i < 26; ++i) {
        for (int j = 0; j < m; ++j) {
            int v = 0;
            if (sb[j] == i) v = 1;
            ht[i].h1 = ht[i].h1 + 1LL * st1[j] * v;
            ht[i].h1 %= mod1;

            ht[i].h2 = ht[i].h2 + 1LL * st2[j] * v;
            ht[i].h2 %= mod2;

            ht[i].n = i;
        }

        ht[i].h1 = ht[i].h1 * st1[1000000] % mod1;
        ht[i].h2 = ht[i].h2 * st2[1000000] % mod2;
        //if (ht[i].h1 > 0 || ht[i].h2 > 0) s.insert(ht);
    }
    sort(ht, ht + 26, cmp_h);

    for (int i = 0; i < 26; ++i) {
        for (int j = 0; j < n; ++j) {
            int v = 0;
            if (sa[j] == i) v = 1;
            hs[i][j].h1 = (j ? hs[i][j - 1].h1 : 0) + 1LL * st1[j] * v;
            hs[i][j].h1 %= mod1;

            hs[i][j].h2 = (j ? hs[i][j - 1].h2 : 0) + 1LL * st2[j] * v;
            hs[i][j].h2 %= mod2;
        }
    }

    for (int pos = 0; pos + m - 1 < n; ++pos) {
        bool is = true;
        int r = pos + m - 1;
        for (int i = 0; i < 26; ++i) {
            h[i].h1 = hs[i][r].h1 - (pos ? hs[i][pos - 1].h1 : 0);
            if (h[i].h1 < 0) h[i].h1 += mod1;
            h[i].h1 = h[i].h1 * st1[1000000 - pos] % mod1;

            h[i].h2 = hs[i][r].h2 - (pos ? hs[i][pos - 1].h2 : 0);
            if (h[i].h2 < 0) h[i].h2 += mod2;
            h[i].h2 = h[i].h2 * st2[1000000 - pos] % mod2;

            h[i].n = i;

            f[i] = h[i];
        }
        for (int i = 0; i < 26; ++i) arr[i] = -1;
        sort(h, h + 26, cmp_h);
        for (int i = 0; i < 26; ++i) {
            if (h[i].h1 > 0 || h[i].h2 > 0) {
                if (ht[i].h1 != h[i].h1 || ht[i].h2 != h[i].h2) {
                    is = false;
                    break;
                }
                arr[h[i].n] = ht[i].n;
            }
        }
        if (!is) continue;
        for (int i = 0; i < 26; ++i) {
            if (arr[i] == -1) continue;
            int to = arr[i];
            if (arr[to] == -1) {
                if (f[to].h1 > 0 || f[to].h2 > 0) {
                    is = false;
                    break;
                }
                continue;
            }
            if (arr[to] != i) {
                is = false;
                break;
            }
        }
        if (is) {
            ans.push_back(pos + 1);
        }
    }
    printf("%d\n", ans.size());
    for (int i = 0; i < ans.size(); ++i) {
        printf("%d ", ans[i]);
    }
    printf("\n");
}
