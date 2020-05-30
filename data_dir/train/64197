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

const int T = 3e5 + 10;

int track[T];
int interval[T];
int ate[T];

int main() {
    ios::sync_with_stdio(false);
    int n,m; cin >> n >> m;
    int x,y;

    for(int i = 0; i < n; i++) {
        cin >> x;
        track[x] = i+1;
    }
    for(int i = 1; i <= n; i++) ate[i] = n;

    int ini,fim;
    for(int i = 0; i < m; i++) {
        cin >> x >> y;
        if(track[x] < track[y]) ini = x, fim = y;
        else ini = y, fim = x;
        ate[track[ini]] = min(ate[track[ini]], track[fim]-1);
    }

    for(int i = n-1; i >= 0; i--)
        if(ate[i] >= ate[i+1]) ate[i] = max(i+1, ate[i+1]);
    
    ll ans = 0;
    for(int i = 1; i <= n; i++) {
        ans += (ate[i]-i+1);
        //cout << i << " " << ate[i] << endl;
    }
    cout << ans << endl;


    return 0;
}

