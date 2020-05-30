#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int D[100];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, k;
    cin>>n>>k;
    for(int i = 0; i < n; ++i)
    {
        int mask = 0;
        for(int j = 0; j < k; ++j)
        {
            int inp;
            cin>>inp;
            mask = mask*2+inp;
        }
        ++D[mask];
    }
    for(int i = 0; i < 100; ++i)
    {
        for(int j = 0; j < 100; ++j)
        {
            if(!(i&j) && D[i] && D[j])
                return cout<<"YES"<<endl, 0;
        }
    }
    cout<<"NO"<<endl;
    return 0;
}
