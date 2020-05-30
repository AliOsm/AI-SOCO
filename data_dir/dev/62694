#include <bits/stdc++.h>
using LL = long long;

int n,m;
LL bad[1<<20];
double dp[1<<20];
std::string str[50];

int main() {
	scanf("%d",&n);
	for (int i = 0; i < n; ++ i) {
		char s[21];
		scanf("%s",s);
		str[i] = s;
	}
	m = str[0].length();
	for (int i = 0; i < n; ++ i) {
		for (int j = i+1; j < n; ++ j) {
			int same = 0;
			for (int k = 0; k < m; ++ k) {
				if (str[i][k] == str[j][k])
					same |= 1<<k;
			}
			bad[same] |= 1ll<<i | 1ll<<j;
		}
	}
	for (int s = (1<<m)-1; s >= 0; -- s) {
		for (int i = 0; i < m; ++ i) {
			if (s>>i&1)
				bad[s^1<<i] |= bad[s];
		}
	}
	for (int s = (1<<m)-1; s >= 0; -- s) {
		int count = 0;
		for (int i = 0; i < m; ++ i) {
			if ((s>>i&1) == 0) {
				dp[s] += dp[s^1<<i];
				count ++;
			}
		}
		if (count > 0)
			dp[s] /= count;
		count = 0;
		for (int i = 0; i < n; ++ i) {
			count += bad[s]>>i&1;
		}
		dp[s] += (double)count/n;
	}
	printf("%.10f\n",dp[0]);
	return 0;
}
