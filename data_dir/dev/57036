#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
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
#define debug(...)
#define pary(...)
#define endl '\n'
#define IOS() ios_base::sync_with_stdio(0);cin.tie(0)
#endif

const ll MOD = 1000000007;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int iNF = 0x3f3f3f3f;
const ll MAXN = 100005;

int n, t, a[MAXN], seg[MAXN * 4];
vector<int> val, pos[MAXN];

void build(int o, int l, int r) {
    if (r == l + 1) {
        seg[o] = a[l];
    } else {
        int mid = (l + r) >> 1;
        build(o<<1, l, mid);
        build(o<<1|1, mid, r);
        seg[o] = __gcd(seg[o<<1], seg[o<<1|1]);
    }
}

int qry (int o, int nL, int nR, int qL, int qR) {
    if (nL >= qR || nR <= qL || qL >= qR) {
        return 0;
    } else if (nL >= qL && nR <= qR) {
        return seg[o];
    } else {
        int mid = (nL + nR) >> 1;
        return __gcd(qry(o<<1, nL, mid, qL, qR), qry(o<<1|1, mid, nR, qL, qR));
    }
}
/********** Good Luck :) **********/
int main()
{
    IOS();
    cin >> n;
    REP (i, n) {
        cin >> a[i];
        val.eb(a[i]);
    }

    sort(ALL(val));
    val.resize(unique(ALL(val))-val.begin());
    REP (i, n) {
        pos[lower_bound(ALL(val),a[i])-val.begin()].eb(i);
    }

    build(1, 0, n);
    pary(seg, seg+n*2);
    
    cin >> t;
    while (t--) {
        int l, r;
        cin >> l >> r;
        l--;
        int gcd = qry(1, 0, n, l, r);
        auto idx = lower_bound(ALL(val), gcd) - val.begin();
        debug(gcd);
        if (idx == SZ(val) || val[idx] != gcd) {
            cout << r - l << endl;
        } else {
            cout << r - l - (lower_bound(ALL(pos[idx]),r) - lower_bound(ALL(pos[idx]),l)) << endl;
        }
    }
    return 0;
}
