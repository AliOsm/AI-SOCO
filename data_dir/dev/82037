#include <bits/stdc++.h>
using namespace std;

int m[368], f[368];

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int n;
	cin >> n;
	while (n--) {
		char c;
		int a, b;
		cin >> c >> a >> b;
		if (c == 'M')
			++m[a], --m[b + 1];
		else
			++f[a], --f[b + 1];
	}
	int ans = 0;
	for (int i = 1; i < 368; ++i) {
		m[i] += m[i - 1], f[i] += f[i - 1];
		ans = max(ans, min(m[i], f[i]));
	}
	cout << 2 * ans;

	return 0;
}
