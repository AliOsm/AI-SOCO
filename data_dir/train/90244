#include <bits/stdc++.h>
#define pii pair<int, int>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;

#define MAXN 100005
#define INF 0x3f3f3f3f

void solve() {
    int n, a, b, k;
    int cg = 0;

    cin >> n >> a >> b >> k;

    vector<int> v;

    for (int i = 0; i < n; i++) {
        int h; cin >> h;
        h = h % (a+b);
        if (h == 0) h += a+b;
        if (h <= a) cg++;
        else {
            v.pb((h-a+a-1)/a);
        }
    }

    sort(v.begin(), v.end());
    for (int x : v) {
        if (k-x >= 0) {
            k -= x;
            cg++;
        }
    }

    cout << cg << '\n';
}

int main(){
#ifdef LOCAL
    freopen("input.txt","r",stdin);
#endif
    ios_base::sync_with_stdio(0); cin.tie(0);

    int t = 1;
    while (t--) {
        solve();
    }

}
