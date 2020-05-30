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

//char cw[4] = {'^', '>', 'v', '<'};
//char ccw[4] = {'^', '<', 'v', '>'};

int dw(char a) {
    if(a == '^') return 0;
    if(a == '>') return 1;
    if(a == 'v') return 2;
    if(a == '<') return 3;
}

int ddw(char a) {
    if(a == '^') return 0;
    if(a == '<') return 1;
    if(a == 'v') return 2;
    if(a == '>') return 3;
}

int main() {
    ios_base::sync_with_stdio(false);
    char a,b;
    int n;
    cin >> a >> b >> n;

    int x = dw(a);
    int xx = ddw(a);
    int y = dw(b);
    int yy = ddw(b);

    bool um = ( ((x+n)%4) == y);
    bool dois = ( ((xx+n)%4) == yy);

    if((um and dois) or (!um and !dois)) cout << "undefined" << endl;
    else if(um) cout << "cw" << endl;
    else cout << "ccw" << endl;

    return 0;
}

