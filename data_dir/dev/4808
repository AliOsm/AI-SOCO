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

const int T = 1e5 + 3;
ll b[T];
ll g[T];

ll maxB = 0;
ll secB = 0;
ll minG = INF;
 
int main() {
    ios_base::sync_with_stdio(false);
    ll n,m; cin >> n >> m;
    
    ll ans = 0;

    for(int i = 0; i < n; i++) {
        cin >> b[i];
        ans += b[i]*m;
    }

    for(int i = 0; i < m; i++) {
        cin >> g[i];
        minG = min(minG, g[i]);
        ans += g[i];
    }

    sort(b,b+n, greater<int>());
    maxB = b[0];
    secB = b[1];

    if(minG < maxB) {
        cout << -1 << endl;
        return 0;
    }

    ans -= maxB*m;

    if(minG != maxB) {
        ans += maxB; 
        ans -= minG;
        ans += minG - secB;
    }

    cout << ans << endl;

    return 0;
}

