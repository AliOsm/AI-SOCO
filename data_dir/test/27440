#include <cstdio>
using namespace std;
const int maxk = 112;
int a[maxk];
int p[maxk];

int main()
{
    int n, m, k;
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 1; i <= k ; ++i) {
        scanf("%d", a + i);
        p[a[i]] = i;
    }

    int q;
    int ans = 0;
    while (scanf("%d", &q) == 1) {
        ans += p[q];
        for (int i = p[q]; i > 1; --i) {
            a[i] = a[i-1];
            p[a[i]] = i;
        }
        a[1] = q;
        p[q] = 1;
    }
    printf("%d\n", ans);

    return 0;
}
