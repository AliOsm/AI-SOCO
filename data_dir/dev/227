#include <bits/stdc++.h>
#define MOD 998244353
#define MAX (ll)(1e6+3)
#define INF (ll)(1e10)
using namespace std;
using ll = long long;
int main () {
	int t;
	cin >> t;
	while (t--) {
		int s, i, e;
		cin >> s >> i >> e;
		s += e;			
		if (s <= i) {
			cout << "0\n";
			continue;
		}
		int ss = (s + i + 2) / 2;
		cout << min (s - ss, e) + 1 << "\n";
	}
}
