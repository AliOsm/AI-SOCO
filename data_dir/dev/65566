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
    ll a,b,c;
    cin >> a >> b >> c;
    if(!c) cout << (a == b? "YES" : "NO") << endl;
    else if(b >= a and c > 0) cout << ((b-a)%c == 0? "YES" : "NO") << endl;
    else if(a >= b and c < 0) cout << (abs(b-a) % abs(c) == 0? "YES" :"NO") << endl;
    else cout << "NO" << endl;
    return 0;
}

