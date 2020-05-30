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
typedef pair<ll,ll> ii;
typedef tuple<int,int,bool> ti;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const ll MOD = 1e9+7;
const int N = 51;

int n,m,k;
int dist[N][N][2];
bool vis[N][N][2];
ll ways[N][N][2];
ll b[N][N];

void pre() {
    for(int i = 0; i < N; i++) b[i][0] = b[i][i] = 1;
    for(int i = 1; i < N; i++)
        for(int j = 1; j < N; j++)
            b[i][j] = (b[i-1][j-1] + b[i-1][j])%MOD;
}

ll choose(int x, int i, int y, int j, bool z) {
    return (((b[x][i]*b[y][j])%MOD)*ways[x][y][z])%MOD;
}

void bfs() {
    queue<ti> fila;
    fila.emplace(n,m,0);
    vis[n][m][0] = 1;
    ways[n][m][0] = 1;

    while(!fila.empty()) {
        int x,y;
        bool z;
        tie(x,y,z) = fila.front();
        fila.pop();
        int oX = n-x, oY = m-y;

        //cout << x << " " << y << " " << z << " = ";
        //cout << ways[x][y][z] << endl;
        for(int i = 0; i <= x; i++) {
            for(int j = 0; j <= y; j++) {
                if(!i and !j) continue;
                if(i*50 + j*100 > k) break;
                int ii = i+oX, jj = j+oY;
                if(!vis[ii][jj][!z]) {
                    vis[ii][jj][!z] = 1;
                    dist[ii][jj][!z] = dist[x][y][z]+1;
                    ways[ii][jj][!z] = (ways[ii][jj][!z]+choose(x,i,y,j,z))%MOD;
                    fila.emplace(ii,jj,!z);
                }
                else if(dist[x][y][z]+1 == dist[ii][jj][!z])
                    ways[ii][jj][!z] = (ways[ii][jj][!z]+choose(x,i,y,j,z))%MOD;
            }
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    pre();
    int tmp;
    cin >> tmp >> k;
    for(int i = 0; i < tmp; i++) {
        int x; cin >> x;
        if(x == 50) n++;
        else m++;
    }
    bfs();
    cout << (vis[n][m][1]?dist[n][m][1]:-1) << " " << ways[n][m][1] << endl;
    return 0;
}

