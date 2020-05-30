#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

LL f(LL n, LL ind)
{
    if(ind <= 0)
        return 0;
    LL t = n;
    while((t & (t&-t)) != t)
        t -= t&-t;
    t = t+t - 1;
    if(ind>=t)
        return n;
    return f(n/2, ind) + (n%2 * (ind>t/2)) + f(n/2, ind-t/2-1);
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL n, l, r;
    cin>>n>>l>>r;
    cout<<f(n, r) - f(n, l-1)<<endl;
    return 0;
}
