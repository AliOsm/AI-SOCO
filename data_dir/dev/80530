//IOI 2021
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ff first
#define ss second

typedef long long ll;
typedef pair<int, int> pii;

ll n, cnt, p;

int main() {
	ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	cin >> n;
	for (ll i = 2; i * i <= n; i++)
		if (n % i == 0) {
			while (n % i == 0)
				n /= i;
			cnt++;
			p = i;
		}
	if (n > 1)
		cnt++, p = n;
	if (cnt == 1)
		cout << p << endl;
	else
		cout << 1 << endl;
	return 0;
}
