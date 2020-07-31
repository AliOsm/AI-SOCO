#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define DEBUG
#ifdef DEBUG
#define debug(...) __f(#__VA_ARGS__, __VA_ARGS__)
    template <typename Arg1>
    void __f(const char* name, Arg1&& arg1){
        cerr << name << " : " << arg1 << std::endl;
    }
    template <typename Arg1, typename... Args>
    void __f(const char* names, Arg1&& arg1, Args&&... args){
        const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
    }
#else
#define debug(...)
#endif
#define FOR(i,a,b)     for(int i=a;i<b;++i)
#define RFOR(i,a,b)     for(int i=a;i>=b;--i)
#define ln         "\n"
#define mp make_pair
#define pb push_back
#define sz(a)    ll(a.size())
#define F first
#define S second
#define all(c)    c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<int,int>
typedef long long ll;
typedef long double ld;
typedef    priority_queue<pii,std::vector<pii>,greater<pii> > revpr;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
// ordered_set X
//K-th smallest
//*X.find_by_order(k-1)
//NO OF ELEMENTS < A
//X.order_of_key(A)

const int L=1e6+7;
int n;
std::map<int, pii> counter;
void printans(int x, int y)
{
    cout<<y-x<<ln;
    FOR(i,x+1,y+1)cout<<i<<" ";
    cout<<ln;
}
void solve(std::vector<ll> a, std::vector<ll> b, int flag)
{
    counter[0] = mp(0,0);
    int cur = 1;
    FOR(i,1,n+1)
    {
        while(b[cur]<a[i])cur++;
        // debug(b[cur], a[i]);
        if(counter.find(b[cur] - a[i]) != counter.end())
        {
            if(flag)
            {
                pii idx = counter[b[cur] - a[i]];
                printans(idx.S, cur);
                printans(idx.F, i);
            }
            else
            {
                pii idx = counter[b[cur] - a[i]];
                printans(idx.F, i);
                printans(idx.S, cur);
            }
            exit(0);
        }
        counter[b[cur]-a[i]] = mp(i,cur);
    }
}
int main()
{
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cin >> n;
        ll x;
        std::vector<ll> a,b;
        a.pb(0);
        b.pb(0);
        FOR(i,1,n+1)
        {
            cin >> x;
            a.pb(x);
            a[i] += a[i-1];
        }
        FOR(i,1,n+1)
        {
            cin >> x;
            b.pb(x);
            b[i] += b[i-1];
        }
        if(b[n] > a[n])solve(a, b, 0);
        else solve(b, a, 1);
        cout<<"-1";
        return 0;
}