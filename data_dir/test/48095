#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[3000];
int ans = 0;
int f(int i = 1)
{
    if(i >= 3000)
        return 0;
    int l = f(2*i);
    int r = f(2*i+1);
    ans += abs(r-l);
    return max(r,l)+A[i];
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    cin>>n;
    for(int i = 2; cin>>A[i]; ++i);
    f();
    cout<<ans<<endl;
    return 0;
}
