#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, ll> pil;
typedef pair<int, ll> pli;
typedef pair<double,double> pdd;
#define SQ(i) ((i)*(i))
#define MEM(a, b) memset(a, (b), sizeof(a))
#define SZ(i) int(i.size())
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define REP1(i,j) FOR(i, 1, j+1, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define ALL(_a) _a.begin(),_a.end()
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define X first
#define Y second
#ifdef tmd
#define TIME(i) Timer i(#i)
#define debug(...) do{\
    fprintf(stderr,"%s - %d (%s) = ",__PRETTY_FUNCTION__,__LINE__,#__VA_ARGS__);\
    _do(__VA_ARGS__);\
}while(0)
template<typename T>void _do(T &&_x){cerr<<_x<<endl;}
template<typename T,typename ...S> void _do(T &&_x,S &&..._t){cerr<<_x<<" ,";_do(_t...);}
template<typename _a,typename _b> ostream& operator << (ostream &_s,const pair<_a,_b> &_p){return _s<<"("<<_p.X<<","<<_p.Y<<")";}
template<typename It> ostream& _OUTC(ostream &_s,It _ita,It _itb)
{
    _s<<"{";
    for(It _it=_ita;_it!=_itb;_it++)
    {
        _s<<(_it==_ita?"":",")<<*_it;
    }
    _s<<"}";
    return _s;
}
template<typename _a> ostream &operator << (ostream &_s,vector<_a> &_c){return _OUTC(_s,ALL(_c));}
template<typename _a> ostream &operator << (ostream &_s,set<_a> &_c){return _OUTC(_s,ALL(_c));}
template<typename _a> ostream &operator << (ostream &_s,deque<_a> &_c){return _OUTC(_s,ALL(_c));}
template<typename _a,typename _b> ostream &operator << (ostream &_s,map<_a,_b> &_c){return _OUTC(_s,ALL(_c));}
template<typename _t> void pary(_t _a,_t _b){_OUTC(cerr,_a,_b);cerr<<endl;}
#define IOS()
#else
#define TIME(i)
#define debug(...)
#define pary(...)
#define endl '\n'
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0)
#endif
class Timer {
private:
    string scope_name;
    chrono::high_resolution_clock::time_point start_time;
public:
    Timer (string name) : scope_name(name) {
        start_time = chrono::high_resolution_clock::now();
    }
    ~Timer () {
        auto stop_time = chrono::high_resolution_clock::now();
        auto length = chrono::duration_cast<chrono::microseconds>(stop_time - start_time).count();
        double mlength = double(length) * 0.001;
        debug(scope_name, mlength);
    }
};

const ll MOD = 1000000007;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int iNF = 0x3f3f3f3f;
const ll MAXN = 1003;

int n, m, s, b, k, h;
int dis[102][102];
int p1[MAXN], a[MAXN], f[MAXN], p2[MAXN], d[MAXN];

vector<int> edge[MAXN];

bool vis[MAXN];
int yp[MAXN], xp[MAXN];

bool dfs (int x) {
    for (auto v : edge[x]) {
        if (!vis[v]) {
            vis[v] = true;
            if (yp[v] == -1 || dfs(yp[v])) {
                yp[v] = x;
                return true;
            }
        }
    }
    return false;
}
/********** Good Luck :) **********/
int main()
{
    TIME(main);
    IOS();

    cin >> n >> m;
    MEM(dis, iNF);
    REP (i, m) {
        int u, v;
        cin >> u >> v;
        dis[u][v] = 1;
        dis[v][u] = 1;
    }

    REP1 (i, n) {
        dis[i][i] = 0;
    }
    REP1 (md, n) {
        REP1 (u, n) {
            REP1 (t, n) {
                if (dis[u][md] != iNF && dis[md][t] != iNF) {
                    dis[u][t] = min(dis[u][t], dis[u][md] + dis[md][t]);
                }
            }
        }
    }

    cin >> s >> b >> k >> h;
    REP (i, s) {
        cin >> p1[i] >> a[i] >> f[i];
    }
    REP (i, b) {
        cin >> p2[i] >> d[i];
    }

    int mat = 0;
    MEM(xp, -1);
    MEM(yp, -1);
    REP (i, s) {
        bool fs = true;
        REP (j, b) {
            if (dis[p1[i]][p2[j]] <= f[i] && a[i] >= d[j]) {
                edge[i].eb(j);
                if (fs && yp[j] == -1) {
                    xp[i] = j;
                    yp[j] = i;
                    mat++;
                    fs = false;
                }
            }
        }
    }

    debug(mat);
    REP (i, s) {
        if (xp[i] == -1) {
            MEM(vis, 0);
            if (dfs(i)) {
                mat++;
            }
        }
    }
    
    debug(mat);

    ll ans = INF;
    REP (i, s + 1) {
        ll cur = ll(i) * h;
        cur += min(mat, s - i) * ll(k);
        ans = min(ans, cur);
    }

    cout << ans << endl;
    return 0;
}
