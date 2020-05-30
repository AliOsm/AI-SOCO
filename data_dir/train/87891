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
using namespace std;
// For ordered_set
using namespace __gnu_pbds;
template <typename T>
using ord_set = tree<T,null_type,less<T>,rb_tree_tag,tree_order_statistics_node_update>;
const ll maxn = 1e5;
const ll inf = 1e9;
const double pi = acos(-1);
V<PII> pt;
PII s;
bool left(PII a){
   if(a.F < s.F)return true;
   return false;
}
bool right(PII a){
   if(a.F > s.F)return true;
   return false;
}
bool up(PII a){
   if(a.S > s.S)return true;
   return false;
}
bool down(PII a){
   if(a.S < s.S)return true;
   return false;
}
int passing(PII a){
   if(a.F < 0 || a.F > inf || a.S < 0 || a.S > inf)return -2;
   int ans = 0;
   for(PII i: pt){
      int ct = 0;
      if(left(a) && left(i))ct++;
      if(right(a) && right(i))ct++;
      if(down(a) && down(i))ct++;
      if(up(a) && up(i))ct++;
      ans+=(ct > 0);
   }
   return ans;
}
int main(){
   int n;
   cin >> n;
   cin >> s.F >> s.S;
   loop(i,0,n){
      PII a;
      cin >> a.F >> a.S;
      pt.pb(a);
   }
   int mx = -1 ;
   PII ans;
   int ct = passing({s.F-1,s.S});
   if(ct > mx){
      mx = ct;
      ans = {s.F-1,s.S};
   }
   ct = passing({s.F+1,s.S});
   if(ct > mx){
      mx = ct;
      ans = {s.F+1,s.S};
   }
   ct = passing({s.F,s.S-1});
   if(ct > mx){
      mx = ct;
      ans = {s.F,s.S-1};
   }
   ct = passing({s.F,s.S+1});
   if(ct > mx){
      mx = ct;
      ans = {s.F,s.S+1};
   }
   cout << mx << "\n";
   cout << ans.F << " " << ans.S;
   return 0;
}