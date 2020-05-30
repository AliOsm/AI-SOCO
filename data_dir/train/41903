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
ll getsteps(ll h,V<ll> arr){
    ll s = 0;
    if(h <= 0)return 0;
    loop(i,0,arr.size()){
        h+=arr[i];
        s++;
        if(h <= 0)return s;
    }
    loop(i,0,arr.size()){
        h+=arr[i];
        s++;
        if(h <= 0)return s;
    }
    loop(i,0,arr.size()){
        h+=arr[i];
        s++;
        if(h <= 0)return s;
    }
    loop(i,0,arr.size()){
        h+=arr[i];
        s++;
        if(h <= 0)return s;
    }
    loop(i,0,arr.size()){
        h+=arr[i];
        s++;
        if(h <= 0)return s;
    }
    loop(i,0,arr.size()){
        h+=arr[i];
        s++;
        if(h <= 0)return s;
    }
        return -1;
}
int main(){
    ll h,n;
    cin >> h >> n;
    unordered_map<ll,int> m;
    V<ll> arr(n);
    ll s = 0;
    ll mn = LLONG_MAX;
    loop(i,0,n){
        cin >> arr[i];
        s+=arr[i];
        m[s] = i+1;
        mn = min(mn,s);
    }
    if(h <= abs(mn) && mn < 0){
        cout << getsteps(h,arr);
        return 0;
    }
    if(s >= 0){
        cout << "-1";
        return 0;
    }
    ll mlt = (h+mn)/abs(s);
    mlt--;
    ll ans = n*mlt;
    h-=(mlt*abs(s));
    // cout << mlt << " " << h << "\n";
    ll a = getsteps(h,arr);
    cout << ans+a;
    return 0;
}