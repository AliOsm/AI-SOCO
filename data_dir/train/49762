#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;



int A[100000];
vector<int> H;
int n, k, x;
int mod = 1e9+7;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>n>>k>>x;
    for(int i = 0; i < n; ++i)
        cin>>A[i];
    sort(A, A+n);
    while(k--)
    {
        LL hash = 0;
        for(int i = 0; i < n; ++i)
        {
            hash += 107*hash + A[i];
            hash %= mod;
        }
        H.push_back(hash);
        int hs = H.size();
        for(int i = 1; hs-1-i >= 0; ++i)
        {
            if(hash == H[hs-i-1])
            {
                k %= i;
                break;
            }
        }
        for(int i = 0; i < n; i+=2)
            A[i] ^= x;
        sort(A, A+n);
    }
    cout<<A[n-1]<<' '<<A[0]<<endl;
    return 0;
}
