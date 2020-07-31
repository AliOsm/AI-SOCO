#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[100000];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        cin>>A[i];
    int g = A[0];
    for(int i = 1; i < n; ++i)
        g = __gcd(g, A[i]);
    if(g > 1)
        return cout<<"YES\n0\n",0;
    if(n==1)
        return cout<<"NO\n",0;
    int ans = 0;
    for(int i = 1; i < n; ++i)
    {
        if(A[i] % 2 == 1 && A[i-1] % 2 == 1)
        {
            A[i] = A[i-1] = 0;
            ++ans;
        }
        if(A[i-1] % 2 == 1)
        {
            ans += 2;
            A[i-1] = 0;
        }
    }
    if(A[n-1]%2 == 1) ans += 2;
    cout<<"YES\n"<<ans<<endl;
    return 0;
}
