#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll count(ll n)
{
    if(n<12)
        return n;
    else
        return count(n/2)+count(n/3)+count(n/4);
}
int main()
{
   int n,p;
   cin>>n>>p;
   vector<pair<int,int> >v(n);
   map<int,int> m;
   for(int i=0;i<n;i++)
   {
    cin>>v[i].first;
   }
   int c=0;
   for(int i=n-1;i>=0;i--)
   {
    if(m[ v[i].first ]==0)
    {
        c++;
        v[i].second=c;
        m[v[i].first]++;
     //   cout<<c;
    }
    else
    {
        c=c;
        v[i].second=c;
    }
   }
   while(p--)
   {
    int x;
    cin>>x;
    cout<<v[x-1].second<<endl;
   }

}