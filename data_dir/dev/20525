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
const int T = 110;
const ll LIM = 3e18;
bool vis[T];
int son[T];
ll v[T];
vector<int> pos[T];
int n;

bool solve(int at, int used) {
    vis[at] = 1;

    if(used == n) { son[at] = 0; return 1; }

    for(auto x : pos[at]) {
        son[at] = x;
        if(solve(x,used+1)) return 1;
    }

    son[at] = vis[at] = 0;
    return 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n;
    for(int i = 1; i <= n; i++) cin >> v[i];

    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++) {
            if(v[i] <= LIM/2 and v[i]*2 == v[j]) pos[i].pb(j);
            if(v[i]%3) continue;
            if(v[i]/3 == v[j]) pos[i].pb(j);
        }


    int i;
    for(i = 1; i <= n; i++)
        if(solve(i,1)) break;

    while(i) {
        cout << v[i] << " ";
        i = son[i];
    }
    cout << endl;

    return 0;
}

