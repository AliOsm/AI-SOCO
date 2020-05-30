#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[200000];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    cin>>n;
    string s;
    cin>>s;
    for(int i = 0; i < n; ++i)
        cin>>A[i];
    int ans = 1e9;
    for(int i = 1; i < n; ++i)
    {
        if(s[i-1] == 'R' && s[i] == 'L')
            ans = min(ans, (A[i]-A[i-1])/2);
    }
    cout<<(ans == 1e9 ? -1 : ans)<<endl;
    return 0;
}
