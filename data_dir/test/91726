#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef pair<double,double> pdd;
#define MEM(a, b) memset(a, (b), sizeof(a))
#define SZ(i) ll(i.size())
#define FOR(i, j, k, in) for (ll i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (ll i=j ; i>=k ; i-=in)
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
// const ll MAXN = 

ll n,m;
vector<ll> a,d;
vector<ll> me;
/********** Good Luck :) **********/
int main()
{
    IOS();
    cin >> n >> m;
    REP (i,n) {
        string st;
        ll strength;
        cin >> st >> strength;
        if (st == "ATK") {
            a.eb(strength);
        } else {
            d.eb(strength);
        }
    }

    REP (i,m) {
        ll d;
        cin >> d;
        me.eb(d);
    }

    sort(ALL(me));
    sort(ALL(a));
    sort(ALL(d));

    ll ans = 0;

    vector<ll> lft;
    /* kill all */
    ll did = 0;
    REP (i,SZ(me)) {
        if (did < SZ(d) && me[i] > d[did]) {
            did++;
        } else {
            lft.eb(me[i]);
        }
    }

    debug(lft,a,d);
    if (did == SZ(d) && SZ(lft) >= SZ(a)) {
        ll sum = 0;
        
        REP (i,SZ(a)) {
            if (lft[SZ(lft)-i-1] >= a[SZ(a)-i-1]) {
                sum += lft[SZ(lft)-i-1] - a[SZ(a)-i-1];
            } else {
                sum = -INF;
                break;
            }
        }
        REP (i,SZ(lft)-SZ(a)) {
            sum += lft[i];
        }
        debug(sum);
        ans = max(ans,sum);
    }

    debug(me);
    /* don't kill all*/
    REP1 (i,min(SZ(me),SZ(a))) { // kill i
        ll sum = 0;
        REP (j,i) {
            if (me[SZ(me)-1-j] >= a[j]) {
                sum += me[SZ(me)-1-j] - a[j];
            } else {
                sum = -INF;
            }
        }
        debug(i,sum);
        ans = max(ans,sum);
    }
    cout << ans << endl;
    return 0;
}
