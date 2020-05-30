#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<n;i++)
#define REP1(i,n) for(int i=1;i<=n;i++)
#define SZ(i) int(i.size())
#ifdef tmd
#define IOS()
#define debug(...) fprintf(stderr,"%s - %d (%s) = ",__PRETTY_FUNCTION__,__LINE__,#__VA_ARGS__);_do(__VA_ARGS__);
template<typename T> void _do(T &&x){cerr<<x<<endl;}
template<typename T, typename ...S> void _do(T &&x, S &&...y){cerr<<x<<", ";_do(y...);}
#else
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define debug(...)
#endif

const int MAXN = 302;
const ll MOD = 1000000007;
const int iNF = 0x3f3f3f3f;

int n, wei[MAXN], yp[MAXN];
bool vis[MAXN];
vector<int> G[MAXN];

bool dfs (int x) {
    if (vis[x]) {
        return false;
    }
    vis[x] = true;
    for (auto y : G[x]) {
        if (yp[y] == -1 || dfs(yp[y])) {
            yp[y] = x;
            return true;
        }
    }
    return false;
}

int S, T, head[MAXN], lev[MAXN], ecnt;

struct Edge {
    int des, flow, cap, nxt;
} edge[MAXN*MAXN*2];

void add_edge (int f, int t, int cap) {
    debug(f, t, cap);
    edge[ecnt++] = {t, 0, cap, head[f]};
    head[f] = ecnt - 1;
    edge[ecnt++] = {f, 0, 0, head[t]};
    head[t] = ecnt - 1;
}

int dfs (int nd, int lim) {
    if (nd == T || lim == 0) {
        return lim;
    }
    for (int id=head[nd]; id!=-1; id=edge[id].nxt) {
        int x = edge[id].des;
        if (lev[x] == lev[nd] + 1 && edge[id].flow < edge[id].cap) {
            int df = dfs(x, min(lim, edge[id].cap-edge[id].flow));
            if (df) {
                edge[id].flow += df;
                edge[id^1].flow -= df;
                return df;
            }
        }
    }
    return 0;
}

bool bfs () {
    queue<int> que;
    memset(lev, -1, sizeof(lev));
    lev[S] = 0;
    que.emplace(S);

    while (que.size()) {
        int cur = que.front();
        que.pop();

        for (int id=head[cur]; id!=-1; id=edge[id].nxt) {
            int x = edge[id].des;
            if (edge[id].flow < edge[id].cap && lev[x] == -1) {
                lev[x] = lev[cur] + 1;
                que.emplace(x);
            }
        }
    }

    return lev[T] != -1;
}

int dinic () {
    int ret = 0;
    while (bfs()) {
        int df = 0;
        while (df = dfs(S, iNF)) {
            ret += df;
        }
    }
    return ret;
}

/*********************GoodLuck***********************/
int main () {
    IOS();

    cin >> n;
    REP1 (i, n) {
        int sz, v;
        cin >> sz;
        REP (j, sz) {
            cin >> v;
            G[i].emplace_back(v);
        }
    }

    memset(yp, -1, sizeof(yp));
    REP1 (i, n) {
        cin >> wei[i];
        wei[i] *= -1;
        memset(vis, 0, sizeof(vis));
        dfs(i);
    }

    S = 0, T = n + 1;

    int sum = 0;
    memset(head, -1, sizeof(head));
    REP1 (i, n) {
        for (auto y : G[i]) {
            if (yp[y] != i) {
                add_edge(i, yp[y], iNF);
            }
        }
        if (wei[i] > 0) {
            sum += wei[i];
            add_edge(S, i, wei[i]);
        } else if (wei[i] < 0) {
            add_edge(i, T, -wei[i]);
        }
    }

    cout << -(sum - dinic()) << endl;
}
