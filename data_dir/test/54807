#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, ans = 1e9;
    cin>>n;
    for(int i = 1; i <= n; ++i)
    {
        int j = n/i+bool(n%i);
        ans = min(i+j, ans);
    }
    cout<<ans*2<<endl;
    return 0;
}
