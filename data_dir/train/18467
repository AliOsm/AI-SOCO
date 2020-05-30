/*Ø¨Ù�Ø³Ù�Ù�Ù� Ø§Ù�Ù�Ù�Ù�Ù�Ù� Ø§Ù�Ø±Ù�Ù�Ø­Ù�Ù�Ù�Ù�Ù� Ø§Ù�Ø±Ù�Ù�Ø­Ù�Ù�Ù�*/


//https://www.spoj.com/problems/DQUERY/
///https://www.youtube.com/watch?v=aZG0I9MM03s&list=PL2q4fbVm1Ik7Ds5cuaoOmExjOQG31kM-p&index=3
//#pragma GCC optimize("O3,unroll-loops")
//#pragma GCC target("avx,avx2,fma")

#include <bits/stdc++.h>
using namespace std;
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const double PI = acos(-1.0);
const ll mod = 1e9 + 7;
//const ll mod = 998244353;


inline void normal(ll &a) { a %= mod; (a < 0) && (a += mod); }
inline ll modMul(ll a, ll b) { a %= mod, b %= mod; normal(a), normal(b); return (a * b) % mod; }
inline ll modAdd(ll a, ll b) { a %= mod, b %= mod; normal(a), normal(b); return (a + b) % mod; }
inline ll modSub(ll a, ll b) { a %= mod, b %= mod; normal(a), normal(b); a -= b; normal(a); return a; }
inline ll modPow(ll b, ll p) { ll r = 1; while (p) { if (p & 1) r = modMul(r, b); b = modMul(b, b); p >>= 1; } return r; }
inline ll modInverse(ll a) { return modPow(a, mod - 2); }
inline ll modDiv(ll a, ll b) { return modMul(a, modInverse(b)); }

#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
#define ss(ch) scanf("%s",ch)
#define pi(x) printf("%d",x)
#define pii(x,y) printf("%d %d",x,y)
#define piii(x,y,z) printf("%d %d %d",x,y,z)
#define pl(x) printf("%lld",x)
#define pll(x,y) printf("%lld %lld",x,y)
#define plll(x,y,z) printf("%lld %lld %lld",x,y,z)
#define ps(ch) printf("%s",ch)
#define F(i,a,b)      for(int i= a; i <= b; i++)
#define R(i,b,a)      for(int i= b; i >= a; i--)

/* for Random Number generate
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
*/
///**
template < typename F, typename S >ostream& operator << ( ostream& os, const pair< F, S > & p ) {return os << "(" << p.first << ", " << p.second << ")";}
template < typename T >ostream &operator << ( ostream & os, const vector< T > &v ) {os << "{"; for (auto it = v.begin(); it != v.end(); ++it) {if ( it != v.begin() ) os << ", "; os << *it;} return os << "}";}
template < typename T >ostream &operator << ( ostream & os, const set< T > &v ) {os << "["; for (auto it = v.begin(); it != v.end(); ++it) {if ( it != v.begin()) os << ", "; os << *it;} return os << "]";}
template < typename F, typename S >ostream &operator << ( ostream & os, const map< F, S > &v ) {os << "["; for (auto it = v.begin(); it != v.end(); ++it) {if ( it != v.begin() ) os << ", "; os << it -> first << " = " << it -> second ;} return os << "]";}
#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)
clock_t tStart = clock();
#define timeStamp dbg("Execution Time: ", (double)(clock() - tStart)/CLOCKS_PER_SEC)
void faltu () { cerr << endl; }
template <typename T>void faltu( T a[], int n ) {for (int i = 0; i < n; ++i) cerr << a[i] << ' '; cerr << endl;}
template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) { cerr << arg << ' '; faltu(rest...); }

// Program showing a policy-based data structure.
#include <ext/pb_ds/assoc_container.hpp> // Common file 
#include <ext/pb_ds/tree_policy.hpp>
#include <functional> // for less 
using namespace __gnu_pbds;

// GNU link : https://goo.gl/WVDL6g
typedef tree<int, null_type, less_equal<int>, rb_tree_tag,
        tree_order_statistics_node_update>
        new_data_set;
// find_by_order(k) â�� à¦«à¦¾à¦�à¦¶à¦¨à¦�à¦¿ kth ordered element à¦�à¦° à¦�à¦�à¦�à¦¾ à¦ªà§�à§�à¦¨à§�à¦�à¦¾à¦° à¦°à¦¿à¦�à¦¾à¦°à§�à¦¨ à¦�à¦°à§�à¥¤ à¦�à¦°à§�à¦¥à¦¾à§� à¦¤à§�à¦®à¦¿ à¦�à¦¾à¦�à¦²à§�à¦� kth à¦�à¦¨à§�à¦¡à§�à¦�à§�à¦¸à§� à¦�à¦¿ à¦�à¦�à§�, à¦¸à§�à¦�à¦¾ à¦�à§�à¦¨à§� à¦«à§�à¦²à¦¤à§� à¦ªà¦¾à¦°à¦�à§�!
// order_of_key(x) â�� à¦«à¦¾à¦�à¦¶à¦¨à¦�à¦¿ x à¦�à¦²à¦¿à¦®à§�à¦¨à§�à¦�à¦�à¦¾ à¦�à§�à¦¨ à¦ªà¦�à¦¿à¦¶à¦¨à§� à¦�à¦�à§� à¦¸à§�à¦�à¦¾ à¦¬à¦²à§� à¦¦à§�à§�à¥¤
//*//**___________________________________________________**/
const int N = 1000006;
const int Block = 555;
int cnt[N];
int a[N], ans[N], res = 0;
int n, m;
struct Mos
{
  int l, r, id;
} Q[N];

bool cmp(Mos x, Mos y)
{
  if (x.l / Block != y.l / Block) //diff. block
    return x.l / Block < y.l / Block;
  return x.r < y.r;//same block
}

void Add(int pos)
{
  if (a[pos] > n)return;
  cnt[a[pos]]++;
  if (cnt[a[pos]] == a[pos])res++;
  if (cnt[a[pos]] == a[pos] + 1)res--;
}

void Remove(int pos)
{
  if (a[pos] > n)return;
  cnt[a[pos]]--;
  if (cnt[a[pos]] == a[pos])res++;
  if (cnt[a[pos]] == a[pos] - 1)res--;
}

int main()
{
  //FASTIO
  ///*
#ifndef ONLINE_JUDGE
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  freopen("error.txt", "w", stderr);
#endif
  //*/

  si(n);
  si(m);
  for (int i = 0; i < n; i++) si(a[i]);

  for (int i = 0; i < m; i++) {
    sii(Q[i].l, Q[i].r);
    Q[i].l--;
    Q[i].r--;
    Q[i].id = i;
  }

  sort(Q, Q + m, cmp);

  int curL = 0, curR = 0;
  for (int i = 0; i < m; i++) {
    int l = Q[i].l;
    int r = Q[i].r;
    while (curL < l) {
      Remove(curL);
      curL++;
    }
    while (curL > l) {
      Add(curL - 1);
      curL--;
    }

    while (curR <= r) {
      Add(curR);
      curR++;
    }
    while (curR > r + 1) {
      Remove(curR - 1);
      curR--;
    }
    ans[Q[i].id] = res;
  }

  for (int i = 0; i < m; i++)
    printf("%d\n", ans[i]);
  return 0;
}