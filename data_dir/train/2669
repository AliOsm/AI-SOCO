#include <bits/stdc++.h>
using namespace std;

long long pos[100005][2];

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n; cin >> n;
	for (int i = 0; i < n; ++i) cin >> pos[i][0] >> pos[i][1];

	if (n & 1) {
		exit((cout << "No" << endl, 0));
	}

	for (int i = 0; i < n; ++i) {
		int j = (i + 1) % n;
		int ii = (i + n / 2) % n;
		int jj = (ii + 1) % n;

		long long dx = pos[j][0] - pos[i][0], dy = pos[j][1] - pos[i][1];
		long long dx2 = pos[jj][0] - pos[ii][0], dy2 = pos[jj][1] - pos[ii][1];

		if (dx != -dx2 || dy != -dy2) {
			exit((cout << "No" << endl, 0));
		}
	}
	cout << "Yes" << endl;
}
