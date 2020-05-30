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

const int T = 2e5 + 4;
int pai[T], peso[T], reach[T];
int n,m,a,b;

void init() {
    for(int i = 0; i <= n; i++) {
        pai[i] = i;
        peso[i] = 1;
        reach[i] = 0;
    }
    reach[a] = 1;
    reach[b] = 2;
}

int find(int x) {
    return (x == pai[x]? x : pai[x] = find(pai[x]));
}

void join(int x, int y) {
    x = find(x);
    y = find(y);
    if(x == y) return;
    if(y == a or y == b) swap(x,y);

    if(x == a or x == b) {
        if(y != a and y != b) reach[y] |= reach[x];
        return;
    }

    if(peso[x] < peso[y]) swap(x,y);
    pai[y] = x;
    peso[x] += peso[y];
    reach[x] |= reach[y];
}

int main() {
    ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    while(tc--) {
        cin >> n >> m >> a >> b;
        init();
        for(int i = 0; i < m; i++) {
            int u,v; cin >> u >> v;
            join(u,v);
        }
        ll g[3] = {-1,-1,0};
        for(int i = 1; i <= n; i++) g[reach[find(i)]-1]++;
        cout << g[0]*g[1] << endl;
    }
    return 0;
}

