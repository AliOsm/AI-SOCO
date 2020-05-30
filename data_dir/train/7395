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
#define all(a) a.begin(),a.end()
using namespace std;

const ll maxn = 1e5;
int n,m;
V<int> ta;
V<int> tb;
V<int> a;
V<int> b;
V<int> lps;

void compute(){
    int i = 1;
    int j = 0;
    while(i < b.size()){
        if(b[i] == b[j]){
            j++;
            lps[i++] = j;
        }else{
            if(j != 0)j = lps[j-1];
            else i++;
        }
    }
}

int main(){
    cin >> n >> m;
    ta = V<int> (n);
    tb = V<int> (m);
    a = V<int> (n-1);
    b = V<int> (m-1);
    loop(i,0,n)cin >> ta[i];
    loop(i,0,m)cin >> tb[i];
    if(m == 1){
        cout << n << "\n";
        return 0;
    }
    loop(i,0,m-1){
        b[i] = tb[i+1] - tb[i];
    }
    loop(i,0,n-1){
        a[i] = ta[i+1] - ta[i];
    }
    int ans = 0;
    if(m == 2){
        loop(i,0,a.size()){
            if(a[i] == b[0])ans++;
        }
        cout << ans;
        return 0;
    }
    // for(int i = 0; i < a.size(); ++i)cout << a[i] << " ";
    // cout << "\n";
    // for(int i = 0; i < b.size(); ++i)cout << b[i] << " ";
    // cout << "\n";
    lps = V<int> (b.size());
    compute();
    int i = 0;
    int j = 0;
    while(i < a.size()){
        // printf("i = %d, a[i] = %d, j = %d, b[j] = %d\n",i,a[i],j,b[j]);
        if(a[i] == b[j]){
            i++;
            j++;
            if(j == b.size()){
                ans++;
                j = lps[j-1];
            }
        }else{
            if(j!=0)j = lps[j-1];
            else i++;
        }
    }
    cout << ans;
  return 0;
}
