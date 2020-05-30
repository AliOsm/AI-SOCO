#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

LL P[256];
LL H[256];
LL C[256];

LL f(LL n)
{
    return max(0LL, n*C[int('B')]-H[int('B')])*P[int('B')]
        + max(0LL, n*C[int('S')]-H[int('S')])*P[int('S')]
        + max(0LL, n*C[int('C')]-H[int('C')])*P[int('C')];
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    string S;
    cin>>S;
    for(char i:S)
        ++C[int(i)];
    cin>>H[int('B')]>>H[int('S')]>>H[int('C')];
    cin>>P[int('B')]>>P[int('S')]>>P[int('C')];
    LL r;
    cin>>r;
    LL mi = 0, ma = 1e13;
    while(mi + 1 < ma)
    {
        LL m = (mi + ma) / 2;
        if(f(m) > r)
            ma = m;
        else
            mi = m;
    }
    cout<<mi<<endl;
    return 0;
}
