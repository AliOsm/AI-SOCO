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

const ll INF = LLONG_MAX;
const int T = 1e5 + 3;
ll cost[T][3];
ll dp[T][4][4];
int choose[T][4][4];
int ans[T];
vector<int> g[T];
int n;

ll solve(int at, int pai, int vo, int b) {
    ll r = dp[at][pai][vo];
    if(r != -1) return r;

    ll ans = INF;

    for(int j = 0; j < 3; j++) {
        if(j == pai or j == vo) continue;
        ll z = cost[at][j];
        for(int i = 0; i < g[at].size(); i++) {
            if(g[at][i] == b) continue;
            z += solve(g[at][i],j,pai,at);
        }
        if(z < ans) {
            choose[at][pai][vo] = j;
            ans = z;
        }
    }

    return r = ans;
}

void print(int at, int pai, int vo, int b) {
    ans[at] = choose[at][pai][vo];
    for(int i = 0; i < g[at].size(); i++) {
        if(g[at][i] == b) continue;
        print(g[at][i],ans[at], pai, at);
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    memset(dp, -1, sizeof dp);
    cin >> n;

    for(int i = 0; i < 3; i++)
        for(int j = 1; j <= n; j++)
            cin >> cost[j][i];

    for(int i = 0; i < n-1; i++) {
        int a,b; cin >> a >> b;
        g[a].pb(b);
        g[b].pb(a);
        if(g[a].size() > 2 or g[b].size() > 2) {
            cout << -1 << endl;
            return 0;
        }
    }
   
    int ini = 0;
    for(int i = 1; i <= n; i++)
        if(g[i].size() == 1) ini = i;

    cout << solve(ini,3,3,0) << endl;
    print(ini,3,3,0);
    for(int i = 1; i <= n; i++) cout << ans[i]+1 << " ";
    cout << endl;

    return 0;
}

