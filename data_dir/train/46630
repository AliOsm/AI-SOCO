#include<bits/stdc++.h>
using namespace std;
const int N = 1e5 + 87;
const int S = sqrt(N) + 0.5;
int a[N],ans[S+1][N];
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> a[i];
    for (int k = 1; k <= S; ++k) {
        for (int i = n; i >= 1; --i) {
            int p = i + a[i] + k;
            ans[k][i] = p > n ? 1 : 1 + ans[k][p];
        }
    }
    int q;
    cin >> q;
    while (q--) {
        int p, k;
        cin >> p >> k;
        if (k > S) {
            int w = 0;
            for (;p <= n;++w)
                p = p + a[p] + k;
            cout << w << '\n';
        } else {
            cout << ans[k][p] << '\n';
        }
    }
}
