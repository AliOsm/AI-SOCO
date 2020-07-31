#include <bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
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

int n, m;
vector<pair<int,int> > a;
vector<vector<pair<int,int> > > qry;
vector<int> ans;

tree<int, int, less<int>, rb_tree_tag, tree_order_statistics_node_update> seq;
/*********************GoodLuck***********************/
int main () {
    IOS();
    cin >> n;
    a.resize(n);
    qry.resize(n+1);

    REP (i, n) {
        cin >> a[i].first;
        a[i].second = i;
    }

    cin >> m;
    REP (i, m) {
        int k, p;
        cin >> k >> p;
        qry[k].emplace_back(p, i);
    }

    sort(a.begin(), a.end(), [&](const pair<int,int> p1, const pair<int,int> p2) {
        return p1.first == p2.first ? p1.second < p2.second : p1.first > p2.first;
    });

    ans.resize(m);
    for (auto p : a) {
        debug(p.first, p.second);
        seq[p.second] = p.first;
        for (auto v : qry[seq.size()]) {
            auto res = seq.find_by_order(v.first-1);
            debug(v.first, v.second, res->second);
            ans[v.second] = res->second;
        }
    }

    REP (i, m) {
        cout << ans[i] << endl;
    }
}
