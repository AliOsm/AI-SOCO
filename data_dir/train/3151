#include <cstdio>

using namespace std;

const int MAXN = 100005;
int n;
long long k;
long long a[MAXN];

long long tree[2 * MAXN + 5];

inline long long merge(long long a, long long b) {
    return (a * b) % k;
}

void build_tree() {
    for (int i = 0; i < n; ++i) {
        tree[i + n] = a[i];
    }
    for (int i = n - 1; i > 0; --i) {
        tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
    }
}

long long query(int l, int r) {
    long long res_left = 1LL;
    long long res_right = 1LL;

    for (int i = l + n, j = r + n; i <= j; i >>= 1, j >>= 1) {
        if ((i & 1) == 1) {
            res_left = merge(res_left, tree[i]);
            i++;
        }

        if ((j & 1) == 0) {
            res_right = merge(tree[j], res_right);
            j--;
        }
    }

    return merge(res_left, res_right);
}

int main() {
    scanf("%d %lld\n", &n, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%lld", a + i);
    }

    build_tree();

    long long ans = 0LL;
    for (int i = 0; i < n; ++i) {
        int lo = 0;
        int hi = i;

        if (query(lo, i) != 0) {
            continue;
        } else if (query(hi, i) == 0) {
            ans += i + 1;
        } else {
            while (lo + 1 < hi) {
                int mid = (lo + hi) / 2;
                if (query(mid, i) == 0) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }

            /*
            printf("i: %d, lo: %d, hi: %d\n", i, lo, hi);
            for (int j = 0; j <= i; ++j) {
                printf("%lld ", query(j, i));
            }
            printf("\n");
            */
            ans += hi;
        }
    }

    printf("%lld\n", ans);

    return 0;
}
