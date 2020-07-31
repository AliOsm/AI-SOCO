#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	ll n, a, b, c;
	cin >> n >> a >> b >> c;
	ll ans = n / a;
	ll x = max(0LL, n - c) / (b - c);
	ans = max(ans, x + (n - x * (b - c)) / a);
	cout << ans;
}
