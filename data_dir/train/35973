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
const int INF = 1e5;

const int T = 1e5 + 2;

int n;
int v[T][2];
int wtf[T][4];

int main() {
    ios::sync_with_stdio(false);
    int q; cin >> q;
    int x,y,ok;
    while(q--) {
        int cima = INF;
        int baixo = -INF;
        int dir = INF;
        int esq = -INF;
        cin >> n;

        for(int i = 0; i < n; i++) {
            cin >> v[i][0] >> v[i][1];
            x = v[i][0], y = v[i][1];
            for(int j = 0; j < 4; j++) {
                cin >> ok;
                wtf[i][j] = ok;
                if(!ok) {
                    if(j == 0) baixo = max(baixo,x); 
                    else if (j == 1) dir = min(dir,y);
                    else if (j == 2) cima = min(cima,x);
                    else esq = max(esq,y);
                }
            }
        }

        bool ans = 1;

        //cout << baixo << " " << cima << " " << esq << " " << dir << endl;

        for(int i = 0; i < n; i++) { 
            x = v[i][0], y = v[i][1];
            if(x <= cima and x >= baixo and y <= dir and y >= esq) continue;

            else {
                for(int j = 0; j < 4; j++) {
                    if(!wtf[i][j]) {
                        if(j == 0) ans &= (x <= cima);
                        else if(j == 1) ans &= (y >= esq);
                        else if(j == 2) ans &= (x >= baixo);
                        else ans &= (y <= dir);
                    }
                }
            }
        }
   
        if(ans) cout << 1 << " " << cima << " " << dir << endl;
        else cout << 0 << endl;

    }

    return 0;
}

