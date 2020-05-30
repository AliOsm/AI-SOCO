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
const int T = 2e5 + 2;

int v[T];
bool ok[T];
int n,k,a,m;

bool check(int x) {
    for(int i = 1; i <= x; i++) ok[v[i]] = 1;

    int qtd = 0;
    int bloks = 0;

    for(int i = 1; i <= n; i++) {
        if(!ok[i]) qtd++;
        else {
            if(qtd >= a) bloks++, qtd -= a;
            bloks += qtd/(a+1);
            qtd = 0;
        }
    }

    if(qtd >= a) bloks++, qtd -= a;
    bloks += qtd/(a+1);
    for(int i = 1; i <= x; i++) ok[v[i]] = 0;

    return bloks < k;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> k >> a >> m;

    for(int i = 1; i <= m; i++) cin >> v[i];

    int l = 0;
    int r = m;
    int ans = -1;

    while(l <= r) {
        int mid = (l+r) >> 1;
        if(check(mid)) ans = mid, r = mid-1;
        else l = mid+1;
    }

    cout << ans << endl;

    return 0;
}

