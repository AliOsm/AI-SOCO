#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int maxn = 1e5+5, sq = sqrt(maxn) + 10, maxk = 22;
int n, q, a[maxn];
int bitcount[sq][maxk][2];
int lazy[sq];
int block, bucket[maxn], start[sq];
int call = 0;

void update(int b) {
    for (int i = 0; i < maxk; i++) {
        for (int j = 0; j < 2; j++) {
            bitcount[b][i][j] = 0;
        }
    }
    for (int i = start[b]; bucket[i] == bucket[start[b]]; i++) {
        a[i] ^= lazy[b];
        for (int j = 0; j < maxk; j++) {
            bool as = a[i] & (1<<j);
            bitcount[b][j][as]++;    
        }
    }
    lazy[b] = 0;
}

ll accum(int b) {
    ll res = 0LL;
    for (int i = 0; i < maxk; i++) {
        bool as = lazy[b] & (1<<i);
        res += (1LL<<i) * bitcount[b][i][as^1];
    }
    /*
    for (int i = start[b]; bucket[i] == bucket[start[b]]; i++) {
        res += (a[i] ^ lazy[b]);
    }
    */
    return res;
}

ll query(int l, int r) {
    ll res = 0LL;
    update(bucket[l]);
    if (bucket[l] != bucket[r]) update(bucket[r]);
    while (bucket[l] == bucket[l-1] && l <= r) {
        res += a[l++];
    }
    while (l <= r && bucket[l] < bucket[r]) {
        res += accum(bucket[l]);
        l += block;
    }
    while (l <= r) {
        res += a[l++];
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    //sqrt decomposition
    block = sqrt(n) + 2;
    bucket[0] = -1;
    for (int i = 1; i <= n; i++) {
        bucket[i] = (i-1)/block;
        if (bucket[i] != bucket[i-1]) {
            start[bucket[i]] = i;
        }
    }
    for (int i = bucket[1]; i <= bucket[n]; i++) {
        update(i);    
    }
    cin >> q;
    while (q--) {
        int t, l, r; cin >> t >> l >> r;
        if (t == 1) {
            cout << query(l,r) << '\n';
        }
        else {
            int x; cin >> x;
            int ll = l;
            while (bucket[l] == bucket[l-1] && l <= r) {
                a[l++] ^= x;
            }
            while (l <= r && bucket[l] < bucket[r]) {
                lazy[bucket[l]] ^= x;
                l += block;
            }
            while (l <= r) {
                a[l++] ^= x;
            }
            update(bucket[ll]);
            if (bucket[ll] != bucket[r]) update(bucket[r]);
            /*
            for (int i = bucket[ll]; i <= bucket[r]; i++) {
                update(i);
            }
            */

            /*
            for (int i = l; i <= r; i++) {
                a[i] ^= x;
            }
            for (int i = bucket[l]; i <= bucket[r]; i++) {
                update(i);
            }
            */
        }
    }

    return 0;
}

