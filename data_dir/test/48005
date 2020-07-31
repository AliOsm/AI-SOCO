#include <iostream>
#include <map>

using namespace std;
using ll = long long;

constexpr int MAXN = 1e6 + 6;
int n, k;
int sieve[MAXN];
int a[MAXN];

void gen_sieve() {
    for (int i = 2; i < MAXN; i += 2)
        sieve[i] = 2;

    for (int i = 3; i < MAXN; i += 2) {
        if (sieve[i] == 0) {
            for (int j = i; j < MAXN; j += 2 * i) {
                sieve[j] = i;
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%d", a + i);
    }

    gen_sieve();

    map<int, int> cf;
    for (int i = 0; i < n; ++i) {
        while (a[i] > 1) {
            int p = sieve[a[i]];
            int ct = 0;
            while (a[i] % p == 0) {
                ++ct;
                a[i] /= p;
            }

            cf[p] = max(ct, cf[p]);
        }
    }

    bool poss = true;
    while (k > 1) {
        int p = sieve[k];
        int ct = 0;
        while (k % p == 0) {
            ++ct;
            k /= p;
        }

        poss &= ct <= cf[p];
    }

    printf("%s\n", poss ? "YES" : "NO");

    return 0;
}
