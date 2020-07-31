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
int n;

bool vis[T];
int ans[T];
ii par[T];

void solve() {
    int i = 1;
    int coloca = 3;
    int check = ans[i];
    while(coloca < n) {
        if(!vis[par[check].fi]) { 
            ans[coloca] = par[check].fi;
            vis[par[check].fi] = true;
        }
        else {
            ans[coloca] = par[check].se;
            vis[par[check].se] = true;
        }
        coloca++;
        check = ans[++i];
    }
}

void first() {
    int iter = 0;
    for(int i = 1; i <= n; i++) {
        if(par[par[i].fi].fi == par[i].se or par[par[i].fi].se == par[i].se) {
            ans[0] = i;
            ans[1] = par[i].fi;
            ans[2] = par[i].se;
            vis[i] = true; vis[par[i].fi] = true; vis[par[i].se] = true;
            return;
        } 
        if(par[par[i].se].fi == par[i].fi or par[par[i].fi].se == par[i].fi) {
            ans[0] = i;
            ans[1] = par[i].se;
            ans[2] = par[i].fi;
            vis[i] = true; vis[par[i].fi] = true; vis[par[i].se] = true;
            return;
        }
    }
}

void read() {
    cin >> n;
    int a,b;
    for(int i = 1; i <= n; i++) {
        cin >> a >> b;
        par[i] = mk(a,b);
    }
}

void print() {
    for(int i = 0; i < n; i++)
        cout << ans[i] << " ";
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    read();
    first();
    solve();
    print();
    return 0;
}

