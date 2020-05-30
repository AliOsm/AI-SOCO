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

const int T = 3e5 + 10;
int v[T];
set<int> inQ;
vector<int> g[T];

int count(int u) {
    int ans = 0;
    for(auto x : g[u])  
        if(inQ.count(x)) ans++;
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    int n, m, u, x;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> v[i];
    for(int i = 0; i < m; i++) {
        cin >> u >> x;
            g[u].pb(x);
    }
    inQ.insert(v[n]);
    int ans = 0;
    for(int i = n-1; i >= 1; i--) {
        int at = v[i];
        if(count(at) == inQ.size()) ans++;
        else inQ.insert(at);
    }
    cout << ans << endl;
    return 0;
}

