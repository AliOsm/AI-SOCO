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
const ll MAXN = 300005;

int n, k, c;
vector<int> var[MAXN];
bool init[MAXN];

int djs[MAXN*2], cnt[MAXN*2], sl[MAXN*2];

int fnd (int x) {
    return djs[x] == x ? x : djs[x] = fnd(djs[x]);
}

void mrg (int x, int y) {
    x = fnd(x), y = fnd(y);
    if (x == y) {
        return;
    }
    djs[x] = y;
    cnt[y] += cnt[x];
    assert(sl[x] * sl[y] != -1);

    if (sl[y] + sl[x] > 0) {
        sl[y] = 1;
    } else if (sl[y] + sl[x] < 0) {
        sl[y] = -1;
    }
}

int cur;

void reset (int x) {
    int c1 = cnt[fnd(x*2)], c2 = cnt[fnd(x*2+1)];
    debug(c1, c2);
    if (sl[fnd(x*2)] == 0) {
        if (c1 < c2) {
            cur -= c1;
        } else {
            cur -= c2;
        }
    } else {
        if (sl[fnd(x*2)] == 1) {
            cur -= c1;
        } else {
            cur -= c2;
        }
    }
}

void chg (int x) {
    int c1 = cnt[fnd(x*2)], c2 = cnt[fnd(x*2+1)];
    debug(c1, c2, sl[fnd(x*2)]);
    if (sl[fnd(x*2)] == 0) {
        if (c1 < c2) {
            cur += c1;
        } else {
            cur += c2;
        }
    } else {
        if (sl[fnd(x*2)] == 1) {
            cur += c1;
        } else {
            cur += c2;
        }
    }
}

int main () {
    TIME(main);
    IOS();

    cin >> n >> k;
    REP1 (i, n) {
        char ch;
        cin >> ch;
        init[i] = ch == '1';
    }
    REP (i, k) {

        int sz;
        cin >> sz;
        REP (j, sz) {
            int d;
            cin >> d;
            var[d].eb(i);
        }
    }
    debug("inputed");

    // init
    REP (i, k) {
        djs[i*2] = i*2; // true
        djs[i*2+1] = i*2+1; // false
        cnt[i*2] = 1;
    }


    REP1 (i, n) {
        if (var[i].size() == 1) {
            int x = var[i][0];
            debug(x);
            reset(x);
            debug(cur);
            if (init[i]) {
                sl[fnd(x*2)] = -1;
                sl[fnd(x*2+1)] = 1;
            } else {
                sl[fnd(x*2)] = 1;
                sl[fnd(x*2+1)] = -1;
            }
            chg(x);
        } else if (SZ(var[i]) == 2) {
            int x = var[i][0], y = var[i][1];
            reset(x);
            if (fnd(x*2) != fnd(y*2) && fnd(x*2) != fnd(y*2+1)) {
                reset(y);
            }

            if (init[i]) {
                mrg(x*2, y*2);
                mrg(x*2+1, y*2+1);
            } else {
                mrg(x*2, y*2+1);
                mrg(x*2+1, y*2);
            }

            chg(x);
        }

        cout << cur << endl;
    }
    return 0;
}
