#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ll n; cin >> n;
    ll sum = n*(n+1)/2;
    ll halfsum = sum/2;
    ll curr = 0;
    for (ll i = n; i >= 1; i--) {
        if (curr + i < halfsum) {
            curr += i;
        }
        else {
            curr = halfsum;        
            break;
        }
    }

    ll ans = abs(curr-(sum-curr));
    cout << ans << '\n';

    return 0;
}

