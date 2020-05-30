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

const int N = 2e5 + 10;
int qtd[N];
int acum[N];

int main() {
    ios::sync_with_stdio(false);
    int n,m; cin >> n >> m;
    int x;
    for(int i = 0; i < n; i++) {
        cin >> x;
        qtd[x]++;
        acum[x] = qtd[x];
    }
    for(int i = 1; i <= m; i++) acum[i] += acum[i-1];

    ll ans = 0;
    for(int i = 1; i <= m; i++) 
        ans += qtd[i] * (acum[m] - acum[i]);
    cout << ans << endl;

    return 0;
}

