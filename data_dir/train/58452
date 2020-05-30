#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#define N 100005
using namespace std;
typedef long long ll;
const ll mod = 1000000007LL;
int t, n;
int s[N];
int dp[N];
int main() {
  cin>>t;
  for (int cas=1; cas<=t; ++cas) {
    cin>>n;
    for (int i = 1; i <= n; ++i) {
      scanf("%d", &s[i]);
    }
    memset(dp, 0, sizeof(dp));
    int ans=1;
    for (int i = n; i >= 1; --i) {
      dp[i] = 1;
      for (int j = 2 * i; j <= n; j += i) {
        if (s[i] < s[j]) dp[i] = max(dp[i], dp[j]+1);
      }
      ans = max(ans, dp[i]);
    }
    cout<<ans<<endl;
  }
  return 0;
}
