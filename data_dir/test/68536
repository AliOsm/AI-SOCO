#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
int main()
{
   ll n,m,k;
   scanf("%lld %lld %lld ",&n,&m,&k);
   ll last = k;
   ll a[m];
   for(ll i=0;i<m;i++)   scanf("%lld",&a[i]);
   ll previous = 0;
   ll ans = 0;
  
   while(1)
   {
       ll temp = upper_bound(a,a+m,k)-a;
       if(temp==previous) 
       {
           ll dummy1 = a[temp] % last ;
           ll dummy2 = k%last;
           if(dummy2>=dummy1)  k = a[temp] + abs(dummy1-dummy2);
           else                k = a[temp] + (last-dummy1) + dummy2;
       }       
       else
       k = k +  temp - previous,ans++; 
       if(temp>=m)  break;
       previous = temp;
   }
   printf("%lld",ans);
}