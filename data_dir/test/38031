// #pragma GCC optimize("no-stack-protector")
// #pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.2,popcnt,abm,mmx,avx,tune=native")
// #pragma GCC diagnostic ignored "-W"

#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<vector>
#include<utility>
#include<functional>
#include<complex>
#include<climits>
#include<random>
#include<thread>

#if __cplusplus >= 201103L
#include<unordered_map>
#include<unordered_set>
#include<tuple>
#endif

// #include<ext/pb_ds/assoc_container.hpp>
// #include<ext/pb_ds/tree_policy.hpp>
// #include<ext/rope>

using namespace std;
// using namespace __gnu_pbds;

#define ll long long
#define ld long double
#define X first
#define Y second
#define pb push_back
#define eb emplace_back
#define pii pair<int,int>
#define vint vector<int>
#define vpii vector<pair<int,int>>
#define SS stringstream
#define PQ priority_queue
#define MS(x,v) memset((x),(v),sizeof(x))
#define RZUNI(x) sort(x.begin(),x.end()), x.resize(unique(x.begin(),x.end())-x.begin())
#define FLH fflush(stdout)
#define CPPinput ios_base::sync_with_stdio(0); cin.tie(0)
#define FIN(fname) freopen(fname,"r",stdin)
#define FOUT(fname) freopen(fname,"w",stdout)

#define tm Ovuvuevuevue
#define y1 Enyetuenwuevue
#define left Ugbemugbem
#define ws Osas
#define dec tetteterette
#define expl explexplexpl
#define data datadetedoto

#define YES cout<<"YES"<<endl
#define NO cout<<"NO"<<endl
#define Yes cout<<"Yes"<<endl
#define No cout<<"No"<<endl

#ifdef WEAK
#include"/home/edison/Coding/cpp/template/debug.cpp"
#define DEB(...) printf(__VA_ARGS__),fflush(stdout)
#define WHR() printf("%s: Line %d",__PRETTY_FUNCTION__,__LINE__),fflush(stdout)
#define LOG(...) printf("%s: Line %d ",__PRETTY_FUNCTION__,__LINE__),printf(__VA_ARGS__),fflush(stdout)
#define DEBUG 1
#define exit(x) cout<<"exit code "<<x<<endl, exit(0)
#else
#define PDE(...) ;
#define DEB(...) ;
#define WHR() ;
#define LOG(...) ;
#define DEBUG 0
#endif

#define lowbit(x) ((x)&(-(x)))

void JIZZ(string output=""){cout<<output; exit(0);}

const ld PI=3.14159265358979323846264338327950288;
const ld eps=1e-10;
const ll mod=1e9+7;

long long dp[10], prv[10];

int main(){
    CPPinput;
    int n; cin >> n; 
    for (int i = 1; i < 10; ++i) prv[i] = -1e18;
    while (n--) {
        for (int i = 0; i < 10; ++i) dp[i] = -1e18;
        int n; cin >> n;
        vector<int> v[5];
        while (n--) {
            int c, d; cin >> c >> d;
            v[c].push_back(d);
        }
        for (int i = 1; i <= 3; ++i) sort(v[i].begin(), v[i].end(), greater<int>());
        for (int i = 1; i <= 3; ++i) v[i].resize(min((int)v[i].size(), 3 / i));
        vector<vector<pair<int, int>>> take = {{}, {{1, 0}}, {{1, 0}, {1, 1}}, {{1, 0}, {1, 1}, {1, 2}}, {{2, 0}}, {{2, 0}, {1, 0}}, {{3, 0}}};
        for (auto &vt : take) {
            bool ok = true;
            for (auto &p : vt) if (p.second >= (int)v[p.first].size()) ok = false;
            if (!ok) continue;
            vector<long long> c;
            for (auto &p : vt) c.push_back(v[p.first][p.second]);
            sort(c.begin(), c.end());
            do {
                for (int i = 0; i < 10; ++i) {
                    int j = i + c.size();
                    if (j >= 10) {
                        dp[j % 10] = max(dp[j % 10], prv[i] + accumulate(c.begin(), c.end(), 0ll) + c[9 - i]);
                    } else {
                        dp[j] = max(dp[j], prv[i] + accumulate(c.begin(), c.end(), 0ll));
                    }
                }
            } while (next_permutation(c.begin(), c.end()));
        }
        for (int i = 0; i < 10; ++i) PDE(i, dp[i]);
        swap(dp, prv);
    }
    cout << *max_element(prv, prv + 10) << endl;
}
