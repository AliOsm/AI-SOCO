#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define X first
#define Y second
#define all(x) x.begin(), x.end()

const int MX = (int)1e5 + 10;
// const int mod = (int)1e9 + 7;

int main(int argc, char* argv[]){

    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(0);

    ll n, m;
    int q;
    cin >> n >> m >> q;

    ll gcd = __gcd(n, m);
    ll whichX = n / gcd;
    ll whichY = m / gcd;

    while(q--){
        ll sx, sy, ex, ey;
        cin >> sx >> sy >> ex >> ey;
        --sy, --ey;
        ll okX = (sx == 1? (sy / whichX) : (sy / whichY));
        ll okY = (ex == 1? (ey / whichX) : (ey / whichY));
        // cout << okX << " " << okY << endl;
        bool ok = okX == okY;
        puts(ok ? "YES" : "NO");
    }
 
    return 0;
}