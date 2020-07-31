/*
chirag11032000
Chirag Thakur
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef double db;
typedef pair < ll, ll > pll;
typedef vector < ll > vll;
typedef vector < vll > matrix;

#define pb push_back
#define debug(x) cout << (#x) << " is " << (x) << endl
#define fast_io() ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0)

const ll mod = 1e9 + 7;
const ll inf = LLONG_MAX;
const ll N = 101;

ll a[N], b[N];

void copy(ll n);

int main() {
    fast_io();
    ll n;
    cin >> n;
    for (ll i = 0; i < n; ++i) {
        cin >> a[i];
    }
    ll best = -inf, curr;
    for (ll i = 0; i < n; ++i) {
        copy(n);
        for (ll j = i; j < n; ++j) {
            b[j] = 1 - b[j];
            curr = accumulate(b, b + n, 0);
            best = max(best, curr);
        }
    }
    cout << best << "\n";
    return 0;
}

void copy(ll n) {
    for (ll i = 0; i < n; ++i) {
        b[i] = a[i];
    }
}
