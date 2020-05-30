#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 106;
int a[maxn];
int dp[maxn][3];
int main()
{
	int n;
	scanf("%d", &n);
	memset(dp[0], 0, 3 * sizeof(int));
	for (int i = 1; i <= n; ++i) {
		scanf("%d", a + i);
		dp[i][0] = 1 + min(min(dp[i-1][0], dp[i-1][1]), dp[i-1][2]);
		dp[i][1] = (a[i] & 1) ? min(dp[i-1][0], dp[i-1][2]) : n + 1;
		dp[i][2] = (a[i] & 2) ? min(dp[i-1][0], dp[i-1][1]) : n + 1;
	}
	printf("%d\n", min(min(dp[n][0], dp[n][1]), dp[n][2]));
}
