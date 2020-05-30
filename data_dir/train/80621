#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int a[3][2];

	for (int i = 0; i < 2; ++i)
		for (int j = 0; j < 3; ++j)
			cin >> a[j][i];

	int cnt = 0;

	for (int i = 0; i < 3; ++i)
		cnt += max(0, a[i][0] - a[i][1]) / 2 - max(0, a[i][1] - a[i][0]);

	if (cnt >= 0)
		cout << "Yes";
	else
		cout << "No";

}
