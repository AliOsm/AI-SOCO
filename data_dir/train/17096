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
const int T = 2e3+2;
int n,h,l,r;
int dp[2][T];

int main() {
    ios_base::sync_with_stdio(false);
    memset(dp,-INF,sizeof dp);
    cin >> n >> h >> l >> r;
    int last = 0;
    dp[0][0] = 0;
    int ans = 0;
    while(n--) {
        int at = !last;
        memset(dp[at],-INF,sizeof dp[at]);
        int x; cin >> x;
        for(int i = 0; i < h; i++) {
            if(dp[last][i] < 0) continue;
            int a = (i+x)%h;
            int b = (i+x-1+h)%h;
            dp[at][a] = max(dp[at][a], dp[last][i]+(a >= l and a <= r));
            dp[at][b] = max(dp[at][b], dp[last][i]+(b >= l and b <= r));
            ans = max({ans,dp[at][a],dp[at][b]});
        }
        last = at;
    }
    cout << ans << endl;
    return 0;
}

