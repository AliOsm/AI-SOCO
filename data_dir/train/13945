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
#define MAXN 25
using namespace std;

struct p{
    ll a,b;
    int i;
    bool operator <(const p &rhs){
        if(rhs.a > a && rhs.b > b)return true;
        return false;
    }
    bool operator >(const p &rhs){
        if(rhs.a < a && rhs.b < b)return true;
        return false;
    }
};

bool cmp(p a, p b){
    if(a.a < b.a)return true;
    if(a.a > b.a)return false;
    if(a.b < b.b)return true;
    if(a.b > b.b)return false;
    return (a.i < b.i);
}

int main(){
    int n;
    ll w,h;
    cin >> n >> w >> h;
    V<p> arr;
    loop(i,0,n){
        p q;
        ll a,b;
        cin >> a >> b;
        q.a = a;
        q.b = b;
        q.i = i+1;
        if(a > w && b > h)arr.pb(q);
    }
    if(arr.size() == 0){
        cout << 0;
        return 0;
    }
    n = arr.size();
    sort(arr.begin(),arr.end(),cmp);
    V<int> dp(n);
    V<p> ans;
    for(int i = 0; i < n; ++i){
        dp[i] = 1;
        for(int j = 0; j < i; ++j){
            if(arr[i] > arr[j])dp[i] = max(dp[i],1+dp[j]);
        }
    }
    int mxi = 0;
    p last = arr[0];
    int c = 0;
    for(int i = 1; i < n; ++i){
        if(dp[i] > dp[mxi]){
            c=dp[i];
            last = arr[i];
            mxi=i;
        }
    }
    ans.pb(last);
    c--;
    for(int i = mxi-1; i >= 0; --i){
        if(arr[i] < last && dp[i] == c){
            ans.pb(arr[i]);
            last = arr[i];
            c--;
        }
    }
    reverse(ans.begin(),ans.end());
    cout << ans.size() << "\n";
    for(auto i: ans){
        cout << i.i << " ";
    }
    return 0;
}