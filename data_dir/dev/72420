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
typedef vector<int> vi;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int T = 102;
bool vis[T];
vi v;

int main() {
    ios_base::sync_with_stdio(false);
    int n; cin >> n;

    for(int i = 0; i < n; i++) {
        int x; cin >> x;
        v.pb(x);
    }
    sort(v.begin(),v.end());

    int ans = 0;

    for(int i = 0; i < n; i++) {
        if(vis[i]) continue;
        ans++;
        for(int j = i; j < n; j++) if(!(v[j]%v[i])) vis[j] = 1;
    }

    cout << ans << endl;

    return 0;
}

