#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
const int MX = 1e2;
pair<ll, ll> ans[MX];
int idx;

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	ll x;
	cin >> x;
	ll a = 0, b = 0;

	for (ll i = 1;; ++i) {
		b += i * i;
		a += i;
		ll dv = (x - b + i * a) / a;
		if (dv < i) break ;
		if (dv * a == (x - b + i * a)) {
			if (dv >= i)
			  ans[idx++] = {i,dv};
		}
	}

	cout << 2 * idx - (ans[idx - 1].first == ans[idx - 1].second) << '\n';
	for (int i = 0; i < idx; ++i)
		cout << ans[i].first << ' ' << ans[i].second << '\n';

	for (int i = idx - 1 - (ans[idx - 1].first == ans[idx - 1].second); i >= 0; --i)
		cout << ans[i].second << ' ' << ans[i].first << '\n';

	return 0;
}
