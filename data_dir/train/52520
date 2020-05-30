#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, ll> pil;
typedef pair<ll, int> pli;
typedef pair<double,double> pdd;
#define SQ(i) ((i)*(i))
#define MEM(a, b) memset(a, (b), sizeof(a))
#define SZ(i) int(i.size())
#define FOR(i, j, k, in) for (int i=j ; i<(k) ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=(k) ; i-=in)
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
#else
#define TIME(i)
#define debug(...)
#define pary(...)
#define endl '\n'
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0)
#endif

const ll MOD = 1000000007;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int iNF = 0x3f3f3f3f;
const ll MAXN = 5003;



namespace FLOW {
    int head[MAXN], ecnt, s, t, cur[MAXN];
    struct Edge {
        int t, cap, flow, nxt;
    } edge[MAXN*5];

    void init () {
        memset(head, -1, sizeof(head));
    }

    int lev[MAXN];

    void add_edge (int f, int g, int cap) {
        edge[ecnt++] = (Edge){g, cap, 0, head[f]};
        head[f] = ecnt-1;
        edge[ecnt++] = (Edge){f, 0, 0, head[g]};
        head[g] = ecnt-1;
    }

    int dfs (int nd, int lim) {
        if (nd == t || lim == 0) {
            return lim;
        }
        for (int &i=cur[nd]; i!=-1; i=edge[i].nxt) {
            int x = edge[i].t;
            if (lev[x]==lev[nd]+1 && edge[i].cap>edge[i].flow) {
                int df = dfs(x, min(lim, edge[i].cap-edge[i].flow));
                if (df > 0) {
                    edge[i].flow += df;
                    edge[i^1].flow -= df;
                    return df;
                }
            }
        }
        return 0;
    }

    bool bfs () {
        memset(lev, -1, sizeof(lev));
        queue<int> que;

        que.emplace(s);
        lev[s] = 0;
        while (que.size()) {
            int nd = que.front();
            que.pop();
            for (int i=head[nd]; i!=-1; i=edge[i].nxt) {
                int x = edge[i].t;
                if (edge[i].cap>edge[i].flow && lev[x]==-1) {
                    lev[x] = lev[nd] + 1;
                    que.emplace(x);
                }
            }
        }

        return lev[t] != -1;
    }

    int dinic (int _s, int _t) {
        s = _s, t = _t;
        int flow = 0;
        while (bfs()) {
            copy(head, head+MAXN, cur);
            int df;
            while (df = dfs(s, MOD)) {
                flow += df;
            }
        }

        return flow;
    }
};


/********** Good Luck :) **********/
int main () {
    TIME(main);
    IOS();

    int n, a, b;
    cin >> n;
    FLOW::init();

    int s = 0;

    cin >> a;
    for (int i=2; i<=a; i++) {
        int p;
        cin >> p;
        FLOW::add_edge(0, i+n, 1);
        FLOW::add_edge(p+n, i+n, MOD);
    }
    REP1 (i, n) {
        int x;
        cin >> x;
        FLOW::add_edge(n+x, i, MOD);
    }

    cin >> b;
    int t = n + a + b + 1;
    debug(a, b);
    for (int i=2; i<=b; i++) {
        int p;
        cin >> p;
        FLOW::add_edge(i+a+n, t, 1);
        FLOW::add_edge(i+a+n, a+n+p, MOD);
    }
    REP1 (i, n) {
        int x;
        cin >> x;
        FLOW::add_edge(i, n+a+x, MOD);
    }

    debug("test");

    cout << (a+b-2) - FLOW::dinic(s,t) << endl;
    return 0;
}
/*
2
3
1 1
2 3
3
1 1
2 3
*/
