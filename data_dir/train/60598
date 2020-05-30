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

const int T = 2e6;
const int N = 1e5 + 3;

ll v[T];
ll acum[T];
ll id[T];
ll sz[T];
ll temp[T];
ll ans[N];

set<int> fr;
vector<int> ok[T];

int main() {
    ios_base::sync_with_stdio(false);
    int servers, tasks;
    cin >> servers >> tasks;

    for(int i = 1; i <= tasks; i++) {
        ll a,b,c; cin >> a >> b >> c;
        v[a] += b; v[a+c] -= b;
        id[a] = i;
        sz[a] = b;
        temp[a] = c;
    }

    for(int i = 1; i <= servers; i++) fr.insert(i);

    for(int i = 1; i < T; i++) {
        v[i] += v[i-1];
        acum[i] += acum[i-1];

        if(ok[i].size()) for(auto x : ok[i]) fr.insert(x);

        if(id[i]) {
            ll x = sz[i];
            if(v[i] - acum[i] > servers) ans[id[i]] = -1, acum[i] += x, acum[i+temp[i]] -= x;
            else {
                while(x--) {
                    ans[id[i]] += *fr.begin();
                    ok[i+temp[i]].pb(*fr.begin());
                    fr.erase(fr.begin());
                }
            }
        }
    }

    for(int i = 1; i <= tasks; i++) cout << ans[i] << endl;

    return 0;
}

