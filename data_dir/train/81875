#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

LL C[52];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL n, k;
    cin>>n>>k;
    C[n+1] = 1;
    C[n] = 1;
    for(int i = n-1; i > 0; --i)
        C[i] = C[i+1] + C[i+2];
    int ind = 1;
    while(ind <= n)
    {
        if(C[ind+1]>=k)
        {
            cout<<ind<<' ';
            ++ind;
        }
        else
        {
            cout<<ind+1<<' '<<ind<<' ';
            k -= C[ind+1];
            ind += 2;
        }
    }
    cout<<endl;
    return 0;
}
