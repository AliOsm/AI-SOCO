#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

LL n,m;

bool f(LL day)
{
    if(day >= n)
        return true;
    if(day <= m)
        return false;
    LL dm = day - m;
    LL dm1 = dm + 1LL;
    if(dm > n * 2 / dm1 ) return true;
    if(dm % 2 == 0)
        dm /= 2LL;
    else
        dm1 /= 2LL;
    return dm * dm1 + m >= n;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin>>n>>m;
    if(m>=n)
    {
        cout<<n<<endl;
        return 0;
    }

    LL l, r;
    r = min((LL)2e9 + m + 2LL, n+9LL);
    l = 0;

    while(r - l > 1)
    {
        LL m = (l + r) / 2;
        if(f(m))
            r = m;
        else
            l = m;
    }
    cout<<r<<endl;

    return 0;
}
