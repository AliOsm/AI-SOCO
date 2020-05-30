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

int dp[510][2050];
int path[510][2050];
int n,m;
int v[510][510];
bool vis[510];


int solve(int at, int mask) {
    if(at == n) return mask;
    if(dp[at][mask] != -1) return dp[at][mask];

    int ans = 0;

    for(int i = 0; i < m; i++) {
        int tmp = solve(at+1, mask ^ v[at][i]);
        if(tmp > ans and !vis[at])  path[at][i] = 1, vis[at] = true;
        ans = max(ans,tmp);
    }

    return dp[at][mask] = ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> m;
    memset(dp, -1, sizeof dp);

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin >> v[i][j];

    if(solve(0,0)) {
        vector<int> ans;
        int at = 0;
        int ini = 0;

        while(at < n) {
            ini = 0; 
            while(path[at][ini] == 0) ini++;
            ans.pb(ini + 1);
            at++;
        }
        cout << "TAK" << endl;
        for(auto x : ans) cout << x << " ";
        cout << endl;
    } else cout << "NIE" << endl;

    return 0;
}

