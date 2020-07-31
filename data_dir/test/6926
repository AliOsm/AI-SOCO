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
const int T = 502;

int n,m,b,mod;
ll dp[T][T];


int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> m >> b >> mod;
    dp[0][0] = 1;
    ll ans = 0;
    int error;

    for(int progs = 0; progs < n; progs++) {
        cin >> error;
        for(int linhas = 1; linhas <= m; linhas++)
            for(int bugs = 0; bugs <= b; bugs++)
                if(bugs - error >= 0)
                    dp[linhas][bugs] = (dp[linhas][bugs] + dp[linhas-1][bugs-error]) % mod;
    }

    for(int i = 0; i <= b; i++) ans = (ans + dp[m][i]) % mod;

    cout << ans << endl;

    return 0;
}

