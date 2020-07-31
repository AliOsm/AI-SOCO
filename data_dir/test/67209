//IOI 2021

#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ff first
#define ss second

typedef long long ll;
typedef pair<int, int> pii;

ll n, p, d, w, x = -1;

int main() {
	ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	cin >> n >> p >> w >> d;
	for (ll i = 0; i < d; i++)
		if ((i * w) % d == p % d && i * w <= p) {
			x = i;
			break;
		}
	if (x == -1)
		return cout << -1, 0;
	ll t = (p / w);
	for (; t >= 0; t--)
		if (t % d == x) {
			x = t;
			break;
		}
	ll y = (p - x * w) / d;
	ll z = n - x - y;
	if (z < 0)
		return cout << -1, 0;
	cout << x << " " << y << " " << z << endl;
	return 0;
}
