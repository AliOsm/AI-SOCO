#include <bits/stdc++.h>
using namespace std;

#define fr(i,n) _back
#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

int main() {
    ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    int n,x,a,b;
    while(tc--) {
        cin >> n >> x >> a >> b;
        if(a > b) swap(a,b);
        int na = max(1,a-x);
        x -= a - na;
        int nb = min(n,b+x);
        cout << nb-na << endl;
    }
    return 0;
}

