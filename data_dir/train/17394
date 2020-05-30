#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define sz(X) (int)(X).size()

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr int MOD = 998244353;
constexpr int root = 3;

int sum(int a, int b) {
    int c = a + b;
    return c >= MOD ? c - MOD : c;
}

int prod(int a, int b) {
    return 1LL * a * b % MOD;
}

int modpow(int b, int e) {
    if (e == 0) return 1;
    if (e & 1) return prod(b, modpow(b, e ^ 1));
    return modpow(prod(b, b), e >> 1);
}

inline int inv(int x) {
    return modpow(x, MOD - 2);
}

void ntt(vi& a, bool invert=false) {
    int n = a.size();
    assert((n & (n - 1)) == 0);
    // bit reversal
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) {
            j ^= bit;
        }
        j ^= bit;

        if (i < j)
            swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        int ang = modpow(root, (MOD - 1) / len);
        if (invert) {
            ang = inv(ang);
        }

        for (int i = 0; i < n; i += len) {
            int h = (len >> 1);
            int w = 1;
            for (int j = 0; j < h; ++j) {
                int u = a[i + j], v = prod(a[i + j + h], w);
                a[i + j] = sum(u, v);
                a[i + j + h] = sum(u, MOD - v);
                w = prod(w, ang);
            }
        }
    }

    if (invert) {
        int inv_n = inv(n);
        for (int& x : a) {
            x = prod(x, inv_n);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n, k;
    cin >> n >> k;

    constexpr int SZ = (1 << 20);
    vi a(SZ, 0);
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        int y = 0;
        while (y == 0) {
            y = rand() % MOD;
        }
        a[x] = y;
    }

    ntt(a);
    for (int i = 0; i < SZ; ++i) {
        if (a[i]) {
            a[i] = modpow(a[i], k);
        }
    }
    ntt(a, true);

    for (int i = 0; i < SZ; ++i) {
        if (a[i] > 0) {
            cout << i << ' ';
        }
    }

    return 0;
}
