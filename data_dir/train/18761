#include <bits/stdc++.h>
//For ordered_set
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define MOD 1000000007
#define test int t; cin>>t; while(t--)
#define init(arr,val) memset(arr,val,sizeof(arr))
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loopr(i,a,b) for(int i=a;i>=b;i--)
#define loops(i,a,b,step) for(int i=a;i<b;i+=step)
#define looprs(i,a,b,step) for(int i=a;i>=b;i-=step)
#define ull unsigned long long int
#define ll long long int
#define P pair
#define PLL pair<long long, long long>
#define PII pair<int, int>
#define PUU pair<unsigned long long int, unsigned long long int>
#define L list
#define V vector
#define D deque
#define ST set
#define MS multiset
#define M map
#define UM unordered_map
#define mp make_pair
#define pb push_back
#define pf push_front
#define MM multimap
#define F first
#define S second
#define IT iterator
#define RIT reverse_iterator
#define FAST ios_base::sync_with_stdio(false);cin.tie();cout.tie();
#define FILE_READ_IN freopen("input.txt","r",stdin);
#define FILE_READ_OUT freopen("output.txt","w",stdout);
#define all(a) a.begin(),a.end()
#define ld long double
#define ds pair<PLL,PLL>
using namespace std;
// For ordered_set
using namespace __gnu_pbds;
template <typename T>
using ord_set = tree<T,null_type,less<T>,rb_tree_tag,tree_order_statistics_node_update>;
const ll maxn = 1e5;
const ll inf = 1e9;
const double pi = acos(-1);

// * ds -> .F.F = distance .F.S allowed distance .S.F left or right .S.S index

int main(){
    int n,m;
    cin >> n >> m;
    V<ll> t(n);
    loop(i,0,n)cin >> t[i];
    sort(all(t));
    V<ll> ans(m);
    priority_queue<ds,V<ds>,greater<ds>> p;
    p.push({{1,LLONG_MAX},{0,0}});
    p.push({{1,LLONG_MAX},{1,n-1}});
    loop(i,1,n){
        ll l = t[i]-t[i-1]-1;
        if(l/2 > 0)p.push({{1,l/2},{1,i-1}});
        if(l/2 + (l&1) > 0)p.push({{1,l/2+(l&1)},{0,i}});
    }
    ll total = 0;
    loop(i,0,m){
        auto a = p.top();
        p.pop();
        if(a.S.F){
            ans[i] = t[a.S.S] + a.F.F;
        }else{
            ans[i] = t[a.S.S] - a.F.F;
        }
        total+=a.F.F;
        a.F.F++;
        if(a.F.F <= a.F.S)p.push(a);
    }
    cout << total << "\n";
    loop(i,0,m)cout << ans[i] << " ";
   return 0;
}