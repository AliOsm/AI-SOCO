/*
lakshaygpt28
Lakshay Gupta
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair < ll, ll > pll;
typedef vector < vector < ll > > matrix;
typedef vector < ll > vll;

#define pb push_back
#define debug(x) cout << (#x) << " is " << (x) << endl
#define fast_io() ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0)

const ll mod = 1e9 + 7;
const ll inf = LLONG_MAX;
const ll N = 1e5 + 10;

ll a[N];
vll rst;

int main() {
    fast_io();
    ll n, k;
    cin >> n >> k;
    ll sum = 0;
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }
    if (sum % k == 0) {
        bool flag = 1;
        ll avg = sum / k;
        ll gr = 0, ans = 0;
        for (ll i = 0; i < n; i++) {
            gr += a[i];
            // debug(gr);
            // debug(a[i]);
            if (gr < avg) {
                // gr += a[i];
                ans++;
            } else if (gr == avg) {
                ans++;
                rst.pb(ans);
                ans = 0;
                gr = 0;
            } else {
                flag = 0;
                break;
            }
        }
        if (flag) {
            cout << "Yes\n";
            for (auto x : rst) {
                cout << x << " ";
            }
            cout << "\n";
            return 0;
        }
    }
    cout << "No\n";
    return 0;
}
