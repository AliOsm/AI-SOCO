#include <cstdio>
using namespace std;
const int maxn = 1925;
char d[maxn];
int main()
{
	int exp;
	d[0] = getchar();
	getchar();
	d[1] = getchar();
	int i;
	for (i = 2; (d[i] = getchar()) != 'e'; ++i);
	d[i == 2 && d[1] == '0' ? 1 : i] = '\0';
	scanf("%d", &exp);
	for (i = 0; d[i] && i <= exp; ++i)
		putchar(d[i]);
	if (d[i]) {
		putchar('.');
		for ( ; d[i]; ++i)
			putchar(d[i]);
	} else if (i <= exp) {
		for ( ; i <= exp; ++i)
			putchar('0');
	}
	putchar('\n');
}
