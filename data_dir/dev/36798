#include <bits/stdc++.h>
using namespace std;

#define LL long long
const LL mod = 1e9 + 7;
LL dp[100005];

int main()
{
    int t,k;
    scanf("%d %d",&t,&k);
    dp[0] = 1;
    for(int i=1;i<=100000;i++){
        dp[i] = (dp[i] + dp[i-1]) % mod;
        if(i >= k) dp[i] = (dp[i] + dp[i-k]) % mod;
    }
    dp[0] = 0;
    for(int i=1;i<=100000;i++) dp[i] = (dp[i] + dp[i-1]) % mod;
    while(t--){
        int x,y;
        scanf("%d %d",&x,&y);
        LL ans = dp[y] - dp[x-1];
        ans = ans % mod;
        if(ans < 0) ans += mod;
        printf("%lld\n",ans);
    }
    return 0;
}
