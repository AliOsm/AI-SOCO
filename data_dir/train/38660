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
// const ll MAXN = 

int a, b;
struct Ans {
    int aw, bw;
    array<pii, 5> score;
    int operator() () {
        return aw - bw;
    }
}ans, cur;

int ca, cb;

int win[5];
bool valid (int g) {
    int ta = a, tb = b;
    int ba = 0, bb = 0;
    bool dc = false;
    REP (i, g) {
        if (win[i] == 1) {
            ta -= i == 4 ? 15 : 25;
            bb += i == 4 ? 13 : 23;
        } else if (win[i] == 2) {
            ta -= i == 4 ? 16 : 26;
            tb -= i == 4 ? 14 : 24;
            dc = true;
        } else if (win[i] == -1) {
            tb -= i == 4 ? 15 : 25;
            ba += i == 4 ? 13 : 23;
        } else {
            ta -= i == 4 ? 14 : 24;
            tb -= i == 4 ? 16 : 26;
            dc = true;
        }
    }

    if (ta < 0 || tb < 0) {
        return false;
    }

    cur.aw = ca, cur.bw = cb;
    if (dc) {
        int d = min(ta, tb);
        ta -= d, tb -= d;

        REP (i, g) {
            if (win[i] == 1) {
                int mx = i == 4 ? 13 : 23;
                cur.score[i].X = i == 4 ? 15 : 25;
                cur.score[i].Y = min(mx, tb);
                tb -= cur.score[i].Y;
            } else if (win[i] == 2) {
                cur.score[i].X = i == 4 ? 16 : 26;
                cur.score[i].Y = i == 4 ? 14 : 24;
                if (dc) {
                    cur.score[i].X += d;
                    cur.score[i].Y += d;
                }
                dc = false;
            } else if (win[i] == -1) {
                int mx = i == 4 ? 13 : 23;
                cur.score[i].Y = i == 4 ? 15 : 25;
                cur.score[i].X = min(mx, ta);
                ta -= min(mx, ta);
            } else {
                cur.score[i].Y = i == 4 ? 16 : 26;
                cur.score[i].X = i == 4 ? 14 : 24;
                if (dc) {
                    cur.score[i].X += d;
                    cur.score[i].Y += d;
                }
                dc = false;
            }
        }
    } else {
        REP (i, g) {
            if (win[i] == 1) {
                int mx = i == 4 ? 13 : 23;
                cur.score[i].X = i == 4 ? 15 : 25;
                cur.score[i].Y = min(mx, tb);
                tb -= cur.score[i].Y;
            } else if (win[i] == -1) {
                int mx = i == 4 ? 13 : 23;
                cur.score[i].Y = i == 4 ? 15 : 25;
                cur.score[i].X = min(mx, ta);
                ta -= min(mx, ta);
            }
        }
    }
    return ta == 0 && tb == 0;
}

void solve (int idx) {
    if (ca == 3 || cb == 3) {
        if (valid(idx)) {
            if (ans() < cur()) {
                ans = cur;
            }
        }
    } else {
        ca++;
        REP1 (i, 2) {
            win[idx] = i;
            solve(idx+1);
        }
        ca--;

        cb++;
        REP1 (i, 2) {
            win[idx] = -i;
            solve(idx+1);
        }
        cb--;
    }
}
/********** Good Luck :) **********/
int main () {
    TIME(main);
    IOS();

    int m;
    cin >> m;
    while (m--) {
        ans.bw = 1000;
        cin >> a >> b;
        solve(0);

        if (ans.bw == 1000) {
            cout << "Impossible" << endl;
        } else {
            cout << ans.aw << ":" << ans.bw << endl;
            REP (i, ans.aw + ans.bw) {
                cout << ans.score[i].X << ":" << ans.score[i].Y << " \n"[i==ans.aw+ans.bw-1];
            }
        }
    }
    return 0;
}
