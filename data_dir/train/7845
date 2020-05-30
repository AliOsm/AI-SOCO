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
typedef tuple<ll,int,int> ti;
typedef vector<ti> vti;
typedef vector<ii> vii;
const ll INF = 1e13;
const double PI = acos(-1.0);

const int T = 2e5 + 5;

int n,m;
vti pq;
ll v[T];

int pai[T];
int sz[T];

void init() {
    for(int i = 1; i <= n; i++) pai[i] = i, sz[i] = 1;
}

int find(int x) {
    return (pai[x] == x? x : pai[x] = find(pai[x]));
}

void join(int x, int y) {
    x = find(x);
    y = find(y);
    if(sz[x] < sz[y]) swap(x,y);
    sz[x] += sz[y];
    pai[y] = x;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    init();
    ll id, mini = INF;

    for(int i = 0; i < n; i++) {
        cin >> v[i];
        if(v[i] < mini) mini = v[i], id = i;
    }


    for(int i = 0; i < n; i++) {
        if(i == id) continue;
        pq.eb(mini+v[i], id+1,i+1);
    }

    while(m--) {
        int x,y;
        ll w;
        cin >> x >> y >> w;
        pq.eb(w,x,y);
    }

    sort(pq.begin(), pq.end());

    ll ans = 0;

    for(int i = 0; i < pq.size(); i++) {
        int x,y;
        ll w;
        tie(w,x,y) = pq[i];

        if(find(x) != find(y)) {
            ans += w;
            join(x,y);
        }
    }

    cout << ans << endl;

    return 0;
}

