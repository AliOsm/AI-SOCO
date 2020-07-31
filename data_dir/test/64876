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
const ll INF = 2e18;
const double PI = acos(-1.0);
const int T = 3e3 + 3;

vector<ll> partido[T];
vector<ll> cheap;
int n,m;

ll check(int x) {
    ll tot = partido[1].size();
    ll price = 0;

    cheap.clear();

    for(int i = 2; i <= m; i++) {
        for(int j = 0; j < partido[i].size(); j++) {
            if(j+1 <= x) cheap.pb(partido[i][j]);
            else price += partido[i][j], tot++;
        }
    }

    sort(cheap.begin(), cheap.end());

    for(int i = 0; i < cheap.size() and tot <= x; i++) {
        price += cheap[i];
        tot++;
    }

    return price;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        int x,y; cin >> x >> y;
        partido[x].pb(y);
    }

    for(int i = 1; i <= m; i++)
        sort(partido[i].begin(), partido[i].end(), greater<int>());

    ll ans = INF;
    for(int i = 0; i <= n; i++) ans = min(ans,check(i));

    cout << ans << endl;


    return 0;
}

