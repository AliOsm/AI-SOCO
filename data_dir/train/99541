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

const int MAXN = 200005;
const ll MOD = 1000000007;

bool vis[MAXN];
vector<int> pz[MAXN];

int t, n;
/*********************GoodLuck***********************/
int main () {
    IOS();

    cin >> t;
    while (t--) {
        cin >> n;

        REP (i, n) {
            int p, m;
            cin >> m >> p;
            pz[m].emplace_back(p);
        }

        int les = n;
        int bt = 0;
        ll ans = 0;
        priority_queue<int, vector<int>, greater<int> > pq;
        for (int i=n; i>=0; i--) {
            for (auto p : pz[i]) {
                pq.emplace(p);
            }
            les -= SZ(pz[i]);
            int lft = i - bt - les;
            REP (i, lft) {
                ans += pq.top();
                pq.pop();
                bt++;
            }
        }

        cout << ans << endl;

        REP (i, n+1) {
            pz[i].clear();
        }
    }
}
