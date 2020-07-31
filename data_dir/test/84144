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

const int T = 3e5 + 5;
int v[T];
 
int main() {
    ios_base::sync_with_stdio(false);
    int n; cin >> n;

    for(int i = 1; i <= n; i++) cin >> v[i];

    int ans = min(v[1],v[n])/(n-1);

    for(int i = 1; i <= n; i++) {
        if(i != 1 && i != n) {
            ans = min(ans, min(v[1],v[i])/(i-1));
            ans = min(ans, min(v[n],v[i])/(n-i));
        }
    }

    cout << ans << endl;
    
    return 0;
}

