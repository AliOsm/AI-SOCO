#include <bits/stdc++.h>
using namespace std;

#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

int main() {
    ios_base::sync_with_stdio(false);
    int n; string s;
    cin >> n >> s;
    int oo = 0;
    int nn = 0;
    int ee = 0;
    int rr = 0;
    int zz = 0;

    for(int i = 0 ; i < n; i++) {
        if(s[i] == 'o') oo++;
        if(s[i] == 'n') nn++;
        if(s[i] == 'e') ee++;
        if(s[i] == 'r') rr++;
        if(s[i] == 'z') zz++;
    }

    while(oo and nn and ee) {
        cout << 1 << " ";
        oo--; nn--; ee--;
    }
    while(zz and ee and rr and oo) {
        cout << 0 << " ";
        zz--; ee--; rr--; oo--;
    }
    cout << endl;


    return 0;
}

