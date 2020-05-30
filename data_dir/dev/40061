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
const int T = 1e5 + 5;
ll v[T];

int main() {
    ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    while(tc--) {

        ll big = 0, sum = 0, s;
        int ans = 1, n;
        ll z = 0;
        cin >> n >> s;

        for(int i = 1; i <= n; i++) {
            cin >> v[i];
            z += v[i];
        }

        if(z <= s) { cout << 0 << endl; continue; }

        for(int i = 1; i <= n; i++) {
            ll x; x = v[i];
            sum += x;
            if(big < x) big = x;
            if(sum-big > s) break;
            if(x == big) ans = i;
        }

        cout << ans << endl;

    }

    return 0;
}

