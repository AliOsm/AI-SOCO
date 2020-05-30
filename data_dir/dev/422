#include <bits/stdc++.h> 
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define sz(x) (int)(x).size()
typedef vector<int> vi;
#define ll long long 
#define int long long
#define ld long double
#define fi first
#define se second
#define pb push_back
#define pii pair<int,int>
#define all(x) (x).begin(), (x).end()
const int MOD = 1e9+7;
int mpow(int a,int b,int p=MOD){a=a%p;int res=1;while(b>0){if(b&1)res=(res*a)%p;a=(a*a)%p;b=b>>1;}return res%p;}
const int N=3e5+300;
const int M=19;
int n,a[M][N],ans[N],pr[N];
int get(int i,int j)
{
  int lol=pr[j-i];
  return min(a[lol][i],a[lol][j-(1<<lol)]);
}
int32_t main(){
      ios_base::sync_with_stdio(false);
      cin.tie(NULL);
      #ifndef ONLINE_JUDGE
      freopen("input.txt", "r", stdin);
      // freopen("output.txt","w",stdout);
      #endif
      for(int i=2;i<N;i++) pr[i]=pr[i/2]+1;
      cin>>n;
      for(int i=0;i<n;i++)
      {
        cin>>a[0][i];
        a[0][i+n]=a[0][2*n+i]=a[0][i];
      }     
      for(int j=0;j<M-1;j++)
      {
        for(int i=0;i+(1LL<<(j+1))<=3*n;i++)
        {
          a[j+1][i]=min(a[j][i],a[j][i+(1<<j)]);
        }
      }
      ans[n-1]=-1;
      int mx=a[0][n-1];
      for(int i=n;i<3*n;i++)
      {
        if(2*a[0][i]<mx)
        {
          ans[n-1]=i-(n-1);
          break;
        }
        mx=max(mx,a[0][i]);
      }
      if(ans[n-1]==-1)
      {
        for(int i=0;i<n;i++) cout<<"-1 ";
        return 0;
      }
      // cout<<get(3,3+4);
      for(int i=n-2;i>=0;i--)
      {
        int l=1,r=ans[i+1]+1;
        // cout<<l<<" "<<r<<"\n";
        while(l<=r)
        {
          int mid=(l+r)/2;
          int o=get(i,i+mid);
          if(a[0][i]<=2*o)
          {
            ans[i]=mid;
            l=mid+1;
          }
          else r=mid-1;
        }
        // cout<<ans[i]<<" ";
        // break;
      }
      for(int i=0;i<n;i++) cout<<ans[i]<<" ";
}
// 11 5 2 7 11 5 2 7 11 5 2 7
// I never lose. I either win or I learn