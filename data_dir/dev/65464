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

const int T = 3e5 + 4;

map<int,int> id; 
vector<int> ve;
int v[T];
int n;
int f[T];
int l[T];

int main() {
    ios_base::sync_with_stdio(false);
    int q; cin >> q;
    while(q--) {
        cin >> n;
        id.clear(); 
        ve.clear();

        for(int i = 0; i < n; i++) {
            cin >> v[i];
            ve.pb(v[i]);
        }

        sort(ve.begin(), ve.end());
        ve.resize(unique(ve.begin(), ve.end()) - ve.begin());
        for(int i = 0; i < ve.size(); i++) id[ve[i]] = i+1, f[i+1] = l[i+1] = 0;
        for(int i = 0; i < n; i++) {
            v[i] = id[v[i]];
            if(!f[v[i]]) f[v[i]] = i+1;
            l[v[i]] = i;
        }

        int m = ve.size();
        int ans = 1;
        int cont = 0;

        for(int i = 1; i <= m; i++) {
            if(f[i] > l[i-1]) cont++;
            else ans = max(ans,cont), cont = 1;
        }

        ans = max(ans,cont);
        cout << m-ans << endl;

    }
    
    return 0;
}

