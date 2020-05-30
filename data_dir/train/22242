#include <bits/stdc++.h>

#define SZ(x) (((int)x.size()))

typedef long long ll;
typedef long double ld;

using namespace std;

int n, m, mod = 1000000007;

ll power(int a, int b, int m)
{
	if (b == 0)
		return 1;
	ll c = power(a, b / 2, m);
	if (b & 1)
		return (((c * c) % m) * a) % m;
	return (c * c) % m;
}

int main()
{
	cin >> n >> m;
	cout << power((power(2, m, mod) + mod - 1) % mod, n, mod);
	return 0;
}
