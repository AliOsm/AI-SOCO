#include <bits/stdc++.h>
using namespace std;

#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
const ll INF = 0x3f3f3f3f3f3f3f;
const double PI = acos(-1.0);

const int T = 2e5 + 2;
ll dist[T][20];
ll v[T];
int n,k;

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> k;

    for(int i = 0; i < n; i++) {
        int x; cin >> x;
        dist[x][0]++;
    }

    for(int i = 0; i < T; i++) {
        int passo = 1;
        int x = i;
        if(dist[x][0]) {
            while(x) {
                dist[x/2][passo++] += dist[i][0];
                x /= 2;
            }
            dist[0][passo] = dist[i][0];
        }
    }

    ll ans = INF;

    for(int i = 0; i < T; i++) {
        ll at = 0;
        ll tmp = 0;
        for(int j = 0; j < 20; j++) {
            at += dist[i][j];
            tmp += dist[i][j] * j;
            if(at >= k) {
                ll sobra = at-k;
                ans = min(ans,tmp - (sobra*j));
                break;
            }
        }
    }

    cout << ans << endl;

    return 0;
}

