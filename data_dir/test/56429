/*
 ____________________________________________________________
|                                                            |
|                   Author: ay2306                           |
|____________________________________________________________|

*/
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
#define ord_set tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update>
using namespace std;
// For ordered_set
using namespace __gnu_pbds;
const ll N = 1e6+2;

int parr[N];
void solve(){
    int n;
    cin >> n;
    unordered_map<ll,ll> m;
    V<ll> arr(n);
    ll res = 1;
    loop(i,0,n){
        unordered_map<ll,ll> tmp;
        ll a;
        cin >> a;
        arr[i] = a;
        while(a > 1){
            ll c = parr[a];
            while(c > 1 && a > 1 && a%c == 0){
                tmp[c]++;
                a/=c;
            }
        }
        for(auto &i: tmp){
            m[i.F] = max(i.S,m[i.F]);
        }
    }
    ll totalFact = 1;
    for(auto &i: m){
        loop(j,0,i.S){
            res*=i.F;
        }
    }
    if(*max_element(all(arr)) == res){
        res*=(*min_element(all(arr)));
        ll a = *min_element(all(arr));
        while(a > 1){
            ll c = parr[a];
            while(c > 1 && a > 1 && a%c == 0){
                m[c]++;
                a/=c;
            }
        }
    }
    for(auto &i: m){
        totalFact *= (i.S + 1);
    }
    if(totalFact != n+2){
        cout << "-1\n";
        return;
    }
    cout << res << "\n";
}

int main(){
    loop(i,2,N){
        if(parr[i] == 0){
            for(int j = 1; i*j < N; ++j)parr[i*j] = i;
        }
    }
    int t;
    cin >> t;
    while(t--)solve();
  return 0;
}
