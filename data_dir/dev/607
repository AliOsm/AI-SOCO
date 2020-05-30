#include <bits/stdc++.h>

using namespace std;
const int MAXN = 200200;
int t, n, k, a[MAXN], sumfreq[2 * MAXN], gte[MAXN], lte[MAXN], ans;

int main()
{
	for(scanf("%d", &t); t--;)
	{
		scanf("%d %d", &n, &k);
		memset(sumfreq, 0, 8 * (k + 1));
		memset(gte, 0, 4 * (k + 1));
		memset(lte, 0, 4 * (k + 1));
		ans = n / 2;
		for(int i = 1; i <= n; ++i)
			scanf("%d", &a[i]);
		for(int i = 1; i <= n / 2; ++i)
		{
			sumfreq[a[i] + a[n - i + 1]]++;
			gte[min(a[i], a[n - i + 1])]++;
			lte[max(a[i], a[n - i + 1])]++;
		}
		
		for(int i = k; i >= 1; --i)
			gte[i - 1] += gte[i];
		for(int i = 1; i <= k; ++i)
			lte[i + 1] += lte[i];

		for(int x = 2; x <= 2 * k; ++x)
		{
			int cur = n / 2 - sumfreq[x];
			if(x <= k)
				cur += gte[x];
			else
				cur += lte[x - k - 1];
			ans = min(ans, cur);
		}
		printf("%d\n", ans);
	}
}
