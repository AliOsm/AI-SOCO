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

int main() {
    ios::sync_with_stdio(false);

    ll s,x1,x2,t1,t2,p,d;
    cin >> s >> x1 >> x2 >> t1 >> t2 >> p >>  d;

    int gol;
    if(x2 > x1) gol = 1;
    else gol = -1;

    ll um, dois;

    um = abs(x1-x2)*t2;

    if(d == gol and gol == 1 and p <= x1) dois = abs(p-x2)*t1; 
    else if(d == gol and gol == -1 and p >= x1) dois = abs(p-x2)*t1; 

    else if(d == gol) {
        ll ini;
        if(d == 1) ini = abs(s-p);
        else ini = p;
        ll fim;
        if(d == 1) fim = x2;
        else fim = s-x2;
        dois = (ini + s + fim)*t1;
    }

    else if(d != gol) {
        ll ini;
        if(d == 1) ini = abs(s-p);
        else ini = p;
        ll fim;
        if(d == -1) fim = x2;
        else fim = s-x2;
        dois = (ini + fim)*t1;
    }

    cout << min(um, dois) << endl; 

    return 0;
}

