#include <bits/stdc++.h>
using namespace std;
int n, m;

inline bool can(long long x) {
	return x / 2 >= n && x / 3 - x / 6 + min(x / 2 - n, x / 6) >= m;
}

int main() {
	cin >> n >> m;
	long long low = 0, high = 1e13, mid, ans;
	while (low <= high) {
		mid = (low + high) >> 1;
		if (can(mid))
			ans = mid, high = mid - 1;
		else
			low = mid + 1;
	}
	cout << ans ;
	return 0;
}
