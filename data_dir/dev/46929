#include <bits/stdc++.h>
#define MAX (ll)(2e5+5)
#define MOD (ll)(1e9 + 7)
#define INF (ll)(1e17 + 5)
#define PI (double)(3.14159265)

using namespace std;
using ll = long long;

int main () {
	int t;
	cin >> t;
	while (t--) {
		ll n, m, o1 = 0, o2 = 0;
		cin >> n;
		for (int i = 0; i < n; i++) {
			int val;
			cin >> val;
			if (val & 1) {
				o1++;
			}
		}
		cin >> m;
		for (int i = 0; i < m; i++) {
			int val;
			cin >> val;
			if (val & 1) {
				o2++;
			}
		}
		cout << (o1 * o2) + (n - o1) * (m - o2) << "\n";
	}
}
		
