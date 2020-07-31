#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[100];
int Z[100];
int O[100];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    cin>>n;
    int ans = 0;
    for(int i = 0; i < n; ++i)
        cin>>A[i];
    for(int i = n-1; i >= 0; --i)
        O[i] = O[i+1] + A[i];
    Z[0] = !A[0];
    for(int i = 1; i < n; ++i)
        Z[i] = Z[i-1] + !A[i];
    for(int i = 0; i < n; ++i)
        ans = max(ans, Z[i] + O[i]);
    cout<<ans<<endl;
    return 0;
}
