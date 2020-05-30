/*
 ____________________________________________________________
|                                                            |
|                   Author: ay2306                           |
|____________________________________________________________|

*/
#include <bits/stdc++.h>
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
using namespace std;

const ll maxn = 1e5;

map<V<ll>,int> mip;

bool comp(V<ll> &a,V<ll> &b){
    return a.size() < b.size();
}
bool comp1(V<ll> &a,V<ll> &b){
    // cout << "{";
    // for(auto i: a)cout << i << " ";
    // cout << "}  {";
    // for(auto i: b)cout << i << " ";
    // cout << "}\n";
    for(int i = 0; i < a.size(); ++i){
        if(a[i] != b[i])return false;
    }
    return true;
}

int main(){
    FAST
    int n,m;
    cin >> n >> m;
    V<V<ll> > arr(n, V<ll> (m,0));
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j)cin >> arr[i][j];
    }
    V<V<ll> > diag1;
    for(int i = 0; i < n; ++i){
        int k = i;
        V<ll> p;
        for(int j = 0; j < m; ++j){
            if(k < 0 || j >= n)break;
            p.pb(arr[k--][j]);
        }
        if(p.size())diag1.pb(p);
    }
    for(int j = 1; j < m; ++j){
        int k = j;
        V<ll> p;
        for(int i = n-1; i >= 0; --i){
            if(i < 0 || k >= m){
                break;
            }
            p.pb(arr[i][k++]);
        }
        if(p.size())diag1.pb(p);
    }
    V<V<ll> > arr1(n, V<ll> (m,0));
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j)cin >> arr1[i][j];
    }
    V<V<ll> > diag2;
    for(int i = 0; i < n; ++i){
        int k = i;
        V<ll> p;
        for(int j = 0; j < m; ++j){
            if(k < 0 || j >= n)break;
            p.pb(arr1[k--][j]);
        }
        if(p.size())diag2.pb(p);
    }
    for(int j = 1; j < m; ++j){
        int k = j;
        V<ll> p;
        for(int i = n-1; i >= 0; --i){
            if(i < 0 || k >= m){
                break;
            }
            p.pb(arr1[i][k++]);
        }
        if(p.size())diag2.pb(p);
    }
    for(int i = 0; i < diag2.size(); ++i){
        sort(diag1[i].begin(),diag1[i].end());
        sort(diag2[i].begin(),diag2[i].end());
        if(!comp1(diag1[i],diag2[i])){
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}