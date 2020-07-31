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

const int T = 2e5 + 5;

queue<ii> l[2];
int ans[2][T], v[T], vis[2][T];
vector<int> g[T];
int n;

void solve(int p) {
    while(!l[p].empty()) {
        ii at = l[p].front();
        l[p].pop();

        if(p == (v[at.fi]&1)) ans[p][at.fi] = at.se;

        for(int i = 0; i < g[at.fi].size(); i++) {
            if(!vis[p][g[at.fi][i]]) {
                vis[p][g[at.fi][i]] = 1;
                l[p].emplace(g[at.fi][i], at.se+1);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> v[i];
        if(v[i]&1) l[0].emplace(i,0), vis[0][i] = 1;
        else l[1].emplace(i,0), vis[1][i] = 1;
        if(i - v[i] >= 0) g[i - v[i]].pb(i);
        if(i + v[i] < n) g[i + v[i]].pb(i);

    }

    solve(0);
    solve(1);

    for(int i = 0; i < n; i++)
        cout << (ans[v[i]&1][i] == 0? -1 : ans[v[i]&1][i]) << " ";
    cout << endl;

    return 0;
}

