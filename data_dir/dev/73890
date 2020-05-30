#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll f(ll n, ll k) {
    ll numTerms = n/k;
    ll last = 1 + (numTerms-1) * k;
    ll ans = 1LL*(1+last)*numTerms/2;
    //cout << k << ": " << ans << '\n';
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ll n; cin >> n;
    set<ll> ans;
    for (ll i = 1; i*i <= n; i++) {
        if (n % i == 0) {
            ans.insert(f(n,i));
            ans.insert(f(n,n/i));
        }
    }
    //output
    for (ll i: ans) {
        cout << i << ' ';
    }
    cout << '\n';
    

    return 0;
}

