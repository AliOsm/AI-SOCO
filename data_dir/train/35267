#include <bits/stdc++.h>
using namespace std;

#define fr(i,n) _back
#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

int main() {
    ios_base::sync_with_stdio(false);
    ll n,a,b,c,d;
    cin >> n >> a >> b >> c >> d;
    ll ans = 0;

    for(ll i = 1; i <= n; i++) {
        ll m = max({a+b+i,a+c+i,c+d+i,b+d+i});
        ll k = min({a+b+i,a+c+i,c+d+i,b+d+i});
        ans += max(0ll,k+n-m);
    }

    cout << ans << endl;

    return 0;
}

