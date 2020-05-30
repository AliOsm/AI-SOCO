#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

unordered_map<LL, int> ma;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL n, inp;
    char c;
    cin>>n;
    for(int i = 0; i < n; ++i)
    {
        cin>>c>>inp;
        LL mask = 0, pow = 1;
        while(inp)
        {
            mask += pow * ((inp%10) & 1);
            inp /= 10;
            pow *= 10;
        }
        if(c == '-')
            --ma[mask];
        else if(c == '+')
            ++ma[mask];
        else
            cout<<ma[mask]<<'\n';
    }
    return 0;
}
