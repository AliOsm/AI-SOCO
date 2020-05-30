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

const int T = 110;
bitset<T> vis;
set<ii> pilha;
vii ans;
int v[T];

int main() {
    ios::sync_with_stdio(false);
    int n, k, x;
    cin >> n >> k;
    for(int i = 0; i < n; i++) {
        cin >> x;
        pilha.insert(ii(x,i));
        v[i] = x;
    }

    int p = 0;
    int maxi = 0;
    int mini = INF;

    while(p < k and pilha.size()) {
        if(pilha.size() == 1) break;

        ii at = *pilha.rbegin();
        pilha.erase(at);
        if(vis[at.se]) continue;
        ii nxt = *pilha.begin();
        pilha.erase(nxt);

        if(at.fi <= nxt.fi+1) continue;

        pilha.insert(ii(at.fi-1,at.se));
        pilha.insert(ii(nxt.fi+1,nxt.se));
        v[at.se]--;
        v[nxt.se]++;

        ans.eb(at.se,nxt.se);
        vis[nxt.se] = 1;
        p++;
    }

    for(int i = 0; i < n; i++) mini = min(mini, v[i]), maxi = max(maxi,v[i]); 
    
    cout << maxi - mini << " " << p << endl;
    for(auto z : ans) cout << z.fi+1 << " " << z.se+1 << endl;

    return 0;
}

