#include <iostream>
#include<bits/stdc++.h>
using namespace std;

long long int a[100001],b[100001];
vector<pair<long long int,long long int> >ans;

int main() 
{
    long long int i,j,n,m,x,y;
    cin>>m>>n>>x>>y;
    for(i=0;i<m;i++)
    cin>>a[i];
    for(i=0;i<n;i++)
    cin>>b[i];
    i=j=0;
    while(i<n && j<m)
    {
        if(b[i]<a[j]-x)
        i++;
        else if(b[i]>a[j]+y)
        j++;
        else
        {
            ans.push_back(make_pair(j+1,i+1));
            i++;
            j++;
        }
    }
    cout<<ans.size()<<endl;
    for(i=0;i<ans.size();i++)
    cout<<ans[i].first<<" "<<ans[i].second<<endl;
    
    return 0;
}