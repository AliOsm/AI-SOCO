#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, k;
    cin>>n>>k;
    int ans = n-k+n-1;
    while(k--)
    {
        int m;
        cin>>m;
        int p, c;
        cin>>p;
        if(p==1)
        while(--m)
        {
            cin>>c;
            if(p+1==c)
                ans-=2;
            else
                break;
            p = c;
        }
        if(m>0)
        while(--m)
            cin>>c;
    }
    cout<<ans<<endl;
    return 0;
}
