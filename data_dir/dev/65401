#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<n;++i)
#define REP1(i,n) for(int i=1;i<=n;++i)
#define SZ(i) int(i.size())
#ifdef tmd
#define IOS()
#define debug(...) fprintf(stderr,"#%d: %s = ",__LINE__,#__VA_ARGS__),_do(__VA_ARGS__);
template<typename T> void _do(T &&x){cerr<<x<<endl;}
template<typename T, typename ...S> void _do(T &&x, S &&...y){cerr<<x<<", ";_do(y...);}
template<typename It> ostream& _printRng(ostream &os,It bg,It ed)
{
    os<<"{";
    for(It it=bg;it!=ed;it++) {
        os<<(it==bg?"":",")<<*it;
    }
    os<<"}";
    return os;
}
template<typename T> ostream &operator << (ostream &os,vector<T> &v){return _printRng(os,v.begin(), v.end());}
template<typename T> void pary(T bg, T ed){_printRng(cerr,bg,ed);cerr<<endl;}
#else
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define debug(...)
#define pary(...)
#endif

const int MAXN = 100005;
const ll MOD = 1000000007;

int n, q, s;
int a[MAXN*4], b[MAXN*4], ncnt, lfid[MAXN];
vector<pair<int,ll> > edge[MAXN*3];

void add_edge (int f, int t, int w) {
    debug(f, t, w);
    edge[f].emplace_back(t, w);
}

void build_index (int o, int l, int r) {
    if (l == r - 1) {
        a[o] = b[o] = ncnt;
        lfid[l] = ncnt;
        ncnt++;
    } else {
        int mid = (l + r) >> 1;
        a[o] = ncnt++;
        b[o] = ncnt++;

        build_index(o<<1, l, mid);
        build_index(o<<1|1, mid, r);


        add_edge(a[o], a[o<<1], 0);
        add_edge(a[o], a[o<<1|1], 0);
        add_edge(b[o<<1], b[o], 0);
        add_edge(b[o<<1|1], b[o], 0);
    }
}

void rtov (int v, int qL, int qR, int w, bool rev, int o, int nL, int nR) {
    if (qL >= nR || qR <= nL || qL >= qR) {
        return;
    } else if (qL <= nL && nR <= qR) {
        if (rev) {
            add_edge(lfid[v], a[o], w);
        } else {
            add_edge(b[o], lfid[v], w);
        }
    } else {
        int nM = (nL + nR) >> 1;
        rtov(v, qL, qR, w, rev, o<<1, nL, nM);
        rtov(v, qL, qR, w, rev, o<<1|1, nM, nR);
    }
}

ll dis[MAXN*3];
bool vis[MAXN*3];
typedef pair<ll,int> pli;

void dijkstra () {
    memset(dis, 0x3f, sizeof(dis));
    dis[lfid[s]] = 0;
    priority_queue<pli, vector<pli>, greater<pli> > pq;
    pq.emplace(0, lfid[s]);

    while (pq.size()) {
        int cur = pq.top().second;
        pq.pop();
        if (vis[cur]) {
            continue;
        }
        vis[cur] = true;

        for (auto p : edge[cur]) {
            if (dis[p.first] > dis[cur] + p.second) {
                dis[p.first] = dis[cur] + p.second;
                pq.emplace(dis[p.first], p.first);
            }
        }
    }
}
/*********************GoodLuck***********************/
int main () {
    IOS();
    cin >> n >> q >> s;
    s--;

    build_index(1, 0, n);
    while (q--) {
        int t;
        cin >> t;
        if (t == 1) {
            int f, T, w;
            cin >> f >> T >> w;
            f--, T--;
            rtov(f, T, T+1, w, true, 1, 0, n);
        } else {
            int v, l, r, w;
            cin >> v >> l >> r >> w;
            v--, l--;
            if (t == 2) {
                rtov(v, l, r, w, true, 1, 0, n);
            } else {
                rtov(v, l, r, w, false, 1, 0, n);
            }
        }
    }
    pary(lfid, lfid+n);

    dijkstra();
    REP (i, n) {
        if (dis[lfid[i]] == 0x3f3f3f3f3f3f3f3f) {
            cout << -1 << " \n"[i==n-1];
        } else {
            cout << dis[lfid[i]] << " \n"[i==n-1];
        }
    }

}
