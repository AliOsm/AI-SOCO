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

const int MAXN = 500005;
const ll MOD = 1000000007;

int q, n;
string s[51];
int fr, ans, cnt;
/*********************GoodLuck***********************/
int main () {
    IOS();

    cin >> q;
    while (q--) {
        cin >> n;
        cnt = 0;
        fr = 0;
        ans = 0;
        REP (i, n) {
            string stt;
            cin >> stt;
            debug(stt);
            int cur = 0;
            for (int k=0; k<SZ(stt)/2; k++) {
                cur += stt[k] != stt[SZ(stt)-k-1];
            }
            debug(cur);
            if (cur == 0) {
                ans++;
            } else {
                cnt+=cur;
            }
            if (SZ(stt) & 1) {
                fr++;
            }
        }

        debug(fr, cnt);
        if (fr > 0 || cnt % 2 == 0) {
            cout << n << endl;
        } else {
            cout << n-1 << endl;
        }


    }

}
