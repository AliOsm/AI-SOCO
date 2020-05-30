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

const int T = 40;
const int N = 1e4 + 5;
int dp[T][N];
int vis[T][N];
int v[T];
int n,vez;

int solve(int at, int sum) {
    if(sum >= n) return sum-n;
    if(at >= 10) return INF;
    if(vis[at][sum] == vez) return dp[at][sum];

    int ans = min(solve(at+1,sum),solve(at+1,sum+v[at]));
    vis[at][sum] = vez;
    return dp[at][sum] = ans;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    int x = 1;
    for(int i = 0; i < 10; i++) {
        v[i] = x, x*=3;
    }
    while(tc--) {
        vez++;
        cin >> n;
        cout << n+solve(0,0) << endl;
    }
    return 0;
}

