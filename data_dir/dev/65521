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

int main(){
  ll n, k;
  cin >> n >> k;
  V<ll> arr(k);
  if(k*(k+1)/2 > n){
    cout << "NO\n";
    return 0;
  }
  if(k == 1){
    cout << "YES\n" << n ;
    return 0;
  }
  if(k == 2){
    ll a,b;
    if(n%2 == 0){a = n/2 - 1; b = n/2+1;}
    if(n%2 == 1){a = n/2; b = n/2+1;}
    if(b > a && b <= 2*a && a+b == n){
      cout << "YES\n" << a << " " << b;
      return 0; 
    }else{
      cout << "NO\n";
    }
    return 0;
  }
  loop(i,0,k)arr[i] = i+1;
  ll rem = n - accumulate(arr.begin(),arr.end(),1LL) + 1;
  // cout << rem << "\n";
  loop(i,0,k){
    arr[i] += (rem/k);
  }
  rem%=k;
  loopr(i,k-1,2){
    if(rem){arr[i]++;rem--;}
    else break;
  }
  arr[k-1]+=rem;
  ll s = accumulate(arr.begin(),arr.end(),1LL) - 1;
  loop(i,1,k){
    if(arr[i] <= arr[i-1] || arr[i] > 2*arr[i-1] || s != n){
      cout << "NO\n";
      return 0;
    }
  }
  cout << "YES\n";
  loop(i,0,k){
    cout << arr[i] << " ";
  }
  return 0;
}
