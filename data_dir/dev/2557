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

const int T = 2e5 + 10;
int v[T];
int track[T];
struct node { int oper, a,b; };
vector<node> ans;
int sentinela;
int pos;
int n;

void pre() {
    int best = 0;
    for(int i = 0; i < n; i++) {
        track[v[i]]++;
        if(track[v[i]] > best) {
            best = track[v[i]];
            sentinela = v[i];
            pos = i;
        }
    }
}

void solve() {
    for(int i = pos-1; i >= 0; i--) {
        if(v[i] < sentinela) ans.pb({1,i,i+1});
        if(v[i] > sentinela) ans.pb({2,i,i+1});
    }
    for(int i = pos + 1; i < n; i++) {
        if(v[i] > sentinela) ans.pb({2,i,i-1});
        if(v[i] < sentinela) ans.pb({1,i,i-1});
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n;
    for(int i = 0; i < n; i++) cin >> v[i];
    pre();
    solve();
    cout << ans.size() << endl;
    for(auto x : ans) cout << x.oper << " " << x.a+1 << " " << x.b+1 << endl;

    return 0;
}

