#include<iostream>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

string S;
int dp[2000][2000];
int count[2000];

bool can(int s, int e)
{
    if(dp[s][e])
        return dp[s][e] == 1;
    if(e-s<2)
        return (dp[s][e] = S[s] == S[e] ? 1 : -1) == 1;
    return (dp[s][e] = S[s] == S[e] && can(s+1, e-1) ? 1 : -1) == 1;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>S;
    int n = S.size();
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j <= i; ++j)
            count[i] += can(j, i);
        if(i)
            count[i] += count[i-1];
    }
    LL ans = 0;
    LL right = 0;
    for(int i = n-1; i > 0; --i)
    {
        right = 0;
        for(int j = i; j < n; ++j)
            right += can(i, j);
        ans += right * count[i-1];
    }
    cout<<ans<<endl;
    return 0;
}
