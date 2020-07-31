#include <bits/stdc++.h> 
using namespace std;
typedef long long ll;

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int n;
	cin >> n;

	if (n < 3) {
		cout << -1;
		return 0;
	}

	if (n & 1) {
		ll m = 1LL * n * n;
		cout << m / 2 << ' ' << m / 2 + 1;
		return 0;
	}

	n /= 2;
	ll m = 1LL * n * n;
	cout << m - 1 << ' ' << m + 1;

}
