#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;

ll n;
string s;

ll solve(ll u) {
    ll j = 0;
    ll x = 0;
    for(ll i = 0; i < n; i = j) {
        while(j < n and s[i] == s[j]) j++;
        x += (j < n? j-i-u: 0);
    }
    cout << endl;
    return x;
}
        
 
int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> s;
    ll ans = (n*(n-1) >> 1);
    ans -= solve(0);
    reverse(s.begin(), s.end());
    ans -= solve(1);
    cout << ans << endl;
    return 0;
}

