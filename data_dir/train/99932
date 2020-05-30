#include <iostream>
#include <algorithm>
using namespace std;

int n, k;
const int MAXN = 2005, MOD = 1000000007;
long long dp[MAXN][MAXN];

int main()
{
	cin >> n >> k;

	for(int i = 1; i <= n; i++)
		dp[1][i] = 1;
	for(int i = 2; i <= k; i++)
		for(int j = 1; j <= n; j++)
		{
			for(int c = j; c <= n; c += j)
				dp[i][c] = (dp[i][c] + dp[i - 1][j]) % MOD;
		}

	long long ans = 0;
	for(int j = 1; j <= n; j++)
		ans = (ans + dp[k][j]) % MOD;

	cout << ans << "\n"; 
	return 0;
}
