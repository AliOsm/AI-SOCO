#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int maxn = 5205;
int n, a[maxn][maxn], pre[maxn][maxn];

int getsum(int x1, int y1, int x2, int y2) {
    return a[x2][y2] - a[x1-1][y2] - a[x2][y1-1] + a[x1-1][y1-1];
}

bool poss(int x) {
    int expt = x*x;
    for (int i = x; i <= n; i += x) {
        for (int j = x; j <= n; j += x) {
            int sum = getsum(i-x+1,j-x+1,i,j);
            if (!(sum == 0 || sum == expt)) return false;
        }
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n/4; j++) {
            char c; cin >> c;
            int x;
            if ('0' <= c && c <= '9') x = c-'0';
            else x = 10 + (c-'A');
            //cout << x << '\n';
            for (int k = 0; k < 4; k++) {
                a[i][(j-1)*4+4-k] = (x & 1) ^ 1;
                x >>= 1;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            //cout << a[i][j] << ' ';
            a[i][j] = a[i][j] + a[i-1][j] + a[i][j-1] - a[i-1][j-1];
        }
        //cout << '\n';
    }

    int ans = 1;
    for (int i = 1; i*i <= n; i++) {
        if (n % i == 0) {
            if (poss(i)) ans = max(ans,i);
            if (poss(n/i)) ans = max(ans,n/i);
        }
    }
    cout << ans << '\n';


    return 0;
}

