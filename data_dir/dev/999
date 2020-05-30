#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif // M_PI
#define endl "\n"
#define S struct
#define X first
#define Y second
#define V vector
#ifndef __linux__
#define LLD "%I64d"
#else
#define LLD "%ll""d"
#endif
#define FOR(x, y, z) for (int x = (y); x < (z); ++x)
#define FORR(x, y, z) for (int x = (y); x > (z); --x)
#define GET(a, n) for (int __i = 0; __i < (n); ++__i) cin >> a[__i];
#define GETM(a, n, m) for (int __i = 0; __i < (n); ++__i) for (int __j = 0; __j < m; ++__j) cin >> a[__i][__j];
#define PRINTM(a, n, m) for (int __i = 0; __i < (n); ++__i) { for (int __j = 0; __j < m; ++__j) cout << a[__i][__j] << " ";  cout << endl; };
#define PRINT(a, n) for (int __i = 0; __i < (n); ++__i) cout << a[__i] << " ";
#define IT(a) a.begin(), a.end()
#define SQR(x) (x) * (x)
#define CASE(a, s) cout << "Case #" << a << ": " << s << endl;
#define DEB(a) cout << #a << " = " << (a) << endl; cout.flush();
#define DEBA(a) for (auto __i: a) cout << __i << " "; cout << endl; cout.flush();
#define IFDEB(b, a) if (b) { cout << #a << " = " << (a) << endl; cout.flush(); }
#define YESNO(cond) cout << ((cond) ? "Yes" : "No") << endl;
#define UMAX(left, right) left = max(left, right);
#define UMIN(left, right) left = min(left, right);
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef pair <LL, LL> PLL;
const int MOD = 1000000007;
void yes() { cout << "Yes" << endl;}
void no() { cout << "No" << endl;}
S Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;
S FAIL { FAIL () { cout << "CHANGE!!!" << endl;}};

int main()
{
    int n;
    cin >> n;
    int l, r;
    cin >> l >> r;
    int m = 0;
    vector<PII> v(n);
    FOR (i, 0, n) {
        cin >> v[i].second;
        m += v[i].second;
        v[i].second = -v[i].second;
    }
    FOR (i, 0, n) {
        cin >> v[i].first;
    }
    sort(IT(v));
    FOR (i, 0, n) {
        v[i].second = -v[i].second;
    }
    l = m - l;
    r = m - r;
    swap(l, r);
    vector<int> dp(m + 1, -1e6);
    dp[0] = 0;
    FOR (i, 0, n) {
        FORR (j, m - v[i].second, -1) {
            if (!v[i].first || !(l <= j + v[i].second && j + v[i].second <= r)) {
                UMAX(dp[j + v[i].second], dp[j]);
            } else {
                UMAX(dp[j + v[i].second], dp[j] + 1);
            }
        }
    }
    cout << *max_element(IT(dp));
}

