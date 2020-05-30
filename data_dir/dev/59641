#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int M = 1e9+7;
ll modexp(ll x, ll n) {
    if (n == 0) return 1;
    if (n == 1) return x%M;
    if (n%2==0) return modexp((x*x)%M,n/2);
    return (x*modexp((x*x)%M,n/2))%M;
}
ll n;
int k;

ll f(ll p) {
    vector<map<ll,ll>> dp(k+1);
    for (ll q = 1; n % q == 0; q *= p) dp[0][q] = q % M;
    for (int K = 1; K <= k; K++) {
        ll total = 0;
        int a;
        for (ll q = 1; n % q == 0; q *= p) {
            if (q == 1) a = 0;
            total = (total + dp[K-1][q]) % M;
            dp[K][q] = (modexp(a+1,M-2) * total) % M;
            a++;
        }
    }
    //cout << "p = " << p << ": " << dp[k].rbegin()->second << '\n';
    return dp[k].rbegin()->second;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n >> k;
    ll ans = 1;
    ll co = n;
    for (ll i = 2; i*i <= n; i++) {
        if (co % i == 0) {
            while (co % i == 0) {
                co /= i;
            }
            ans = (ans * f(i)) % M;
        }
    }
    if (co > 1) ans = (ans * f(co)) % M;
    cout << ans << '\n';

    return 0;
}

