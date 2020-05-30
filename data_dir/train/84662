#include<bits/stdc++.h>
using namespace std;
#define mem(a,b) memset(a, b, sizeof(a) )
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a) * (a))

#define IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define fraction() cout.unsetf(ios::floatfield); cout.precision(10); cout.setf(ios::fixed,ios::floatfield);

map<int, int>m;
//set<int>s;
int ar[101];
int main()
{
    IO
   int n,k;
   cin >>n >> k;
   for(int i = 1; i <= n; i++)
   {
       int a;
       cin >>a;
       m[a] = i;
   }
   if(m.size() < k)cout<<"NO";
   else
   {
       cout<<"YES"<<endl;
       map<int, int>:: iterator it;
       int cnt = 0;
       for(it = m.begin(); it != m.end(); it++)
       {
           cnt++;
           if(cnt > k)break;

           cout<<it->second<<" ";
       }
   }
}
