#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, begin, end) for (__typeof(begin) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define pb push_back
#define eb emplace_back
#define ALL(x) (x).begin(), (x).end()
#define X first
#define Y second
// read integers
int RI() {return 0;}
template<typename T>
int RI(T & a)
{
	int c;
	int s = 1;
	while (!((c = getchar()) == '-' || isdigit(c) || c == EOF));
	if (c == EOF)
		return 0;
	if (c == '-') {
		s = -1;
		c = getchar();
	}
	a = 0;
	do {
		a = 10 * a + s * (c - '0');
	} while (isdigit(c = getchar()));
	return 1;
}
template<typename T, typename... Args>
int RI(T & a, Args & ... args) {return RI(a) ? 1 + RI(args...) : 0;}
//print integers, python style
template<typename T>
void __PI(T a)
{
	static const int maxd = 25;
	static char d[maxd];
	int i = maxd - 1;
	int s = a < 0 ? -1 : 1;
	do {
		d[--i] = s * (a % 10) + '0';
	} while (a /= 10);
	if (s < 0)
		d[--i] = '-';
	fputs(d + i, stdout);
}
template<char sep>
void __PSI() {}
template<char sep, typename T>
void __PSI(const T & a) {putchar(sep), __PI(a);}
template<char sep, typename T, typename... Args>
void __PSI(const T & a, const Args & ... args) {__PSI<sep, T>(a), __PSI<sep, Args...>(args...);}
template<char sep = ' ', char end = '\n', typename T, typename... Args>
void PI(const T & a, const Args & ... args) {__PI(a), __PSI<sep, Args...>(args...), putchar(end);}

const int maxx = (1 << 7);
double p[maxx], ans[maxx], tmp[maxx];
void upd(double * a, double * b)
{
	rep(i,0,maxx) {
		tmp[i] = 0.0;
		rep(j,0,maxx)
			tmp[i] += a[j] * b[i^j];
	}
	rep(i,0,maxx)
		a[i] = tmp[i];
}
int main()
{
	int n, x;
	RI(n, x);
	rep(i, 0, x+1)
		scanf("%lf", p + i);
	bool first = true;
	while (n) {
		if (n & 1) {
			if (!first)
				upd(ans, p);
			else {
				first = false;
				rep(i, 0, maxx)
					ans[i] = p[i];
			}
		}
		upd(p, p);
		n >>= 1;
	}
	printf("%.16f\n", 1.0-ans[0]);
}
