#include <bits/stdc++.h>
using namespace std;
const int maxn = 2.28e5;
int a[maxn];
int v[maxn];
int to[maxn];
int find(int x) {return to[x] == x ? x : to[x] = find(to[x]);}
int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
		scanf("%d", a + i);
	for (int i = 1; i <= n + 1; ++i)
		to[i] = i;
	int m;
	scanf("%d", &m);
	while (m--) {
		int c;
		scanf("%d", &c);
		if (c == 1) {
			int p, x;
			scanf("%d%d", &p, &x);
			while (x && (p = find(p)) <= n)
				if (v[p] + x < a[p]) {
					v[p] += x;
					x = 0;
				} else {
					x -= a[p] - v[p];
					v[p] = a[p];
					to[p] = p + 1;
				}
		} else {
			int k;
			scanf("%d", &k);
			printf("%d\n", v[k]);
		}
	}
}
