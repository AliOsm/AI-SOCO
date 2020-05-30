#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;
const  int T = 1e3 + 10;
int v[T];
int d[T];

int main() {
    ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    for(int i = 0; i < n; i++) cin >> v[i];
    for(int i = 0; i < m; i++) cin >> d[i];

    int top = 0;
    int ans = 0;
    for(int i = 0; i < n; i++) {
        if(top == m) break;
        if(v[i] <= d[top]) { ans++; top++; }
    }

    cout << ans << endl;

    return 0;
}

