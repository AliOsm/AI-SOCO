#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

LL ans;
void f(LL x)
{
    LL t = x;
    int s = 0;
    while(t)
    {
        s += t % 10;
        t /= 10;
    }
    t = ans;
    while(t)
    {
        s -= t % 10;
        t /= 10;
    }
    if(s>0)
        ans = x;
    else if(s == 0)
        ans = max(ans, x);
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL x;
    cin>>x;
    f(x);
    LL n = 1;
    while(n <= x/10)
    {
        n *= 10;
        f(x/n*n-1);
    }
    cout<<ans<<endl;
    return 0;
}
