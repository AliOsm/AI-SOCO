#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<n;i++)
#define REP1(i,n) for(int i=1;i<=n;i++)
#define SZ(i) int(i.size())
#ifdef tmd
#define IOS()
#define debug(...) fprintf(stderr,"%s - %d (%s) = ",__PRETTY_FUNCTION__,__LINE__,#__VA_ARGS__);_do(__VA_ARGS__);
template<typename T> void _do(T &&x){cerr<<x<<endl;}
template<typename T, typename ...S> void _do(T &&x, S &&...y){cerr<<x<<", ";_do(y...);}
#else
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define debug(...)
#endif

const int MAXN = 10;
const ll MOD = 1000000007;

double dp[MAXN*MAXN];
int h[MAXN][MAXN];
int id[MAXN][MAXN];
pair<int,int> pos[MAXN*MAXN];


int getID (pair<int,int> p) {
    return id[p.first][p.second];
}

int climbLadder (int d) {
    pair<int,int> cur = pos[d];
    cur.first -= h[cur.first][cur.second];
    return getID(cur);
}

/*********************GoodLuck***********************/
int main () {
    IOS();
    REP (i, MAXN) {
        REP (j, MAXN) {
            cin >> h[i][j];
        }
    }

    int idx = 0;
    for (int i=MAXN-1; i>=0; i--) {
        if (i&1) {
            for (int j=0; j<MAXN; j++) {
                id[i][j] = idx;
                pos[idx++] = {i, j};
            }
        } else {
            for (int j=MAXN-1; j>=0; j--) {
                id[i][j] = idx;
                pos[idx++] = {i, j};
            }
        }
    }

    dp[MAXN*MAXN-1] = 0;
    for (int i=98; i>=0; i--) {
        int valid = min(MAXN*MAXN-1 - i, 6);
        double sum = 0;
        for (int j=1; j<=valid; j++) {
            // debug(i, j, climbLadder(i+j));
            sum += min(dp[i+j], dp[climbLadder(i+j)]);
        }

        dp[i] = (6 / double(valid)) + sum / valid;
    }

    cout << fixed << setprecision(10) << dp[0] << endl;
}
