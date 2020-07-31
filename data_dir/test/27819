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
    int a,b,x; cin >> a >> b >> x;
    int last = (a>=b?1:0);
    while(x) {
        if(last) cout << 0,a--;
        else cout << 1,b--;
        x--;
        last = !last;
    }

    if(!last) {
        while(a) cout << 0, a--;
        while(b) cout << 1, b--;
    } else {
        while(b) cout << 1, b--;
        while(a) cout << 0, a--;
    }

    return 0;
}

