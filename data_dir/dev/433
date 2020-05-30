#include <bits/stdc++.h>

using namespace std;

int n, m, x, y, ans, aux[7];

int main()
{
	scanf("%d %d", &n, &m);
	x = y = 1;
	for(int i = 7; i < n; i *= 7)
		x++;
	for(int i = 7; i < m; i *= 7)
		y++;
	if(x + y > 7)
		printf("0\n"), exit(0);
	for(int i = 0, j, k, l, flg; i < n; ++i)
		for(j = 0; j < m; ++j)
		{
			flg = true;
			memset(aux, 0, sizeof aux);
			for(k = 0, l = i; k < x; ++k, l /= 7)
			{
				flg = flg && !aux[l % 7];
				aux[l % 7] = true;
			}
			for(k = 0, l = j; k < y; ++k, l /= 7)
			{
				flg = flg && !aux[l % 7];
				aux[l % 7] = true;
			}
			if(!flg)
				continue;
			ans++;
		}
	printf("%d\n", ans);
}