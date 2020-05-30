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
const int T = 5e3+2;
int dp[T][T];
int v[T], p[T], g[T];
int n,k;

int solve(int at, int times) {
    if(times > k) return -INF;
    if(at >= n) return 0;

    int &r = dp[at][times];
    if(~r) return r;

    r = max(solve(at+1,times), solve(p[at],times+1)+g[at]);

    return r;
}

int main() {
    ios_base::sync_with_stdio(false);
    memset(dp, -1, sizeof dp);
    cin >> n >> k;

    for(int i = 0; i < n; i++) cin >> v[i];
    sort(v,v+n);
    v[n] = 2e9;

    for(int i = 0; i < n; i++) {
        p[i] = upper_bound(v,v+n,v[i]+5) - v;
        g[i] = p[i]-i;
    }

    cout << solve(0,0) << endl;

    return 0;
}

