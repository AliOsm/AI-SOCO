#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int MOD = 998244353;
int n, k;
const int n_ = 501;
int memo[2][n_][n_];
int mx_conseq;
int memo2[n_][n_];
int queries[n_];
int mx_rows;

int dp2(int row, int same)
{
    if(row == n - 1) return same <= mx_rows;
    if(same > mx_rows) return 0;
    int &ret = memo2[row][same];
    if(ret != -1) return ret;

    // put same
    ret = 0;
    if(same + 1 <= mx_rows)
    {
        ret = dp2(row + 1, same + 1);
    }
    ret += dp2(row + 1, 1);
    if(ret >= MOD) ret -= MOD;
    return ret;
}
int solve(int conseq)
{
    mx_rows = min(n, (k + conseq - 1) / conseq - 1);
    if(queries[mx_rows] == -1) {
        memset(memo2, -1, sizeof memo2);
        return queries[mx_rows] = dp2(0, 1);
    }
    return queries[mx_rows];
}
int dp(int reached, int col, int conseq)
{
    if(col == n - 1)
    {
        return reached ? solve(mx_conseq) : 0;
    }
    int &ret = memo[reached][col][conseq];
    if(ret != -1) return ret;

    ret = 0;
    // make it same
    if(conseq + 1 <= mx_conseq)
    {
        ret = dp(reached || conseq + 1 == mx_conseq, col + 1, conseq + 1);
    }
    // change it
    ret += dp(reached, col + 1, 1);
    if(ret >= MOD) ret -= MOD;
    return ret;
}
int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
    cin >> n >> k;
    ll res = 0;
    memset(queries, -1, sizeof queries);
    for(mx_conseq = 1; mx_conseq < min(n + 1, min(501, k)); mx_conseq++) {
        memset(memo, -1, sizeof memo);
        ll here = 2 * dp(mx_conseq == 1, 0, 1);
        if(here >= MOD) here -= MOD;
        res += here;
        if(res >= MOD) res -= MOD;
    }
    cout << res << "\n";
}