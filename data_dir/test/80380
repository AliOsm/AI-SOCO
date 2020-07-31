#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL n;
    cin>>n;
    LL save = n;
    ++n;
    while(true)
    {
        LL t = 1;
        while(n%(t*10) == 0)
            t *= 10;
        if(n/t<10)
            break;
        n += t;
    }
    cout<<n-save<<endl;
    return 0;
}
