#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
#define F first
#define S second
const int N = 5e5+87;
int n;
vector<pii> g[N];
pii t[N*4];
vector<int> tp;
int ans[N];
pii meld(pii a,pii b)
{
    return {a.F?a.F:b.F,a.S+b.S};
}
void init(int o=1,int l=1,int r=n+1)
{
    if (r - l == 1) {
        t[o] = {l,0};
        return;
    }
    int m = (l + r) / 2;
    init(o+o,l,m);
    init(o+1+o,m,r);
    t[o] = meld(t[o+o],t[o+o+1]);
}
pii qry(int i,int j,int o=1,int l=1,int r=n+1)
{
    if (j<=l||r<=i)
        return {0,0};
    if (i <= l && r <= j)
        return t[o];
    int m=(l+r)/2;
    return meld(qry(i,j,o+o,l,m),qry(i,j,o+o+1,m,r));
}
void del(int i,int o=1,int l=1,int r=n+1)
{
    if (r-l==1) {
        t[o].F=0;
        return;
    }
    int m=(l+r)/2;
    if (i < m)
        del(i,o+o,l,m);
    else
        del(i,o+o+1,m,r);
    t[o]=meld(t[o+o],t[o+o+1]);
}
void add(int i,int v,int o=1,int l=1,int r=n+1)
{
    if (r-l==1) {
        t[o].S+=v;
        return;
    }
    int m=(l+r)/2;
    if (i < m)
        add(i,v,o+o,l,m);
    else
        add(i,v,o+o+1,m,r);
    t[o]=meld(t[o+o],t[o+o+1]);
}
bool topo(int u)
{
    del(u);
    add(u,1);
    for (pii e : g[u]) {
        while (1) {
            pii p = qry(e.F,e.S);
            if (p.S)
                return 1;
            if (!p.F)
                break;
            if (topo(p.F))
                return 1;
        }
    }
    add(u,-1);
    tp.push_back(u);
    return 0;
}
void solve()
{
    cin >> n;
    tp.clear();
    for (int i = 1; i <= n; ++i) {
        g[i].clear();
    }
    for (int i = 1; i <= n; ++i) {
        int x;
        cin >> x;
        if (x == -1)
            continue;
        g[i].emplace_back(i+1,x);
        g[x].emplace_back(i,i+1);
    }
    init();
    for (int i = 1; i <= n; ++i) {
        if (qry(i,i+1).F) {
            if (topo(i)) {
                cout << "-1\n";
                return;
            }
        }
    }
    for (int i = 0; i < n; ++i)
        ans[tp[i]]=i+1;
    for (int i = 1; i <= n; ++i)
        cout << ans[i] << " \n"[i==n];
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) solve();
}
