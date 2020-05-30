#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;
const int maxn = 1e5 + 228;
const ll inf = 2e15;
int c[maxn];
ll dp[2][2];
string rev(string s)
{
	for (int i = 0, j = s.size() - 1; i < j; ++i, --j)
		swap(s[i], s[j]);
	return s;
}
int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> c[i];
	string p, s;
	int j = 0;
	dp[0][1] = c[0];
	for (int i = 0; i < n; ++i, p = s, j ^= 1) {
		cin >> s;
		if (i) {
			dp[j][0] = dp[j][1] = inf;
			dp[j][0] = min(dp[j][0], s >= p ? dp[j^1][0] : inf);
			dp[j][0] = min(dp[j][0], s >= rev(p) ? dp[j^1][1] : inf);
			s = rev(s);
			dp[j][1] = min(dp[j][1], (s >= p ? dp[j^1][0] : inf) + c[i]);
			dp[j][1] = min(dp[j][1], (s >= rev(p) ? dp[j^1][1] : inf) + c[i]);
			s = rev(s);
		}
	}
	j^=1;
	ll ans = min(dp[j][0], dp[j][1]);
	cout << (ans < inf ? ans : -1) << '\n';
}
