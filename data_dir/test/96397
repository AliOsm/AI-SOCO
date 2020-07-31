#include <bits/stdc++.h>

using namespace std;

const int base = 3291;

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

	int n;
	string s1, s2;
	cin >> n >> s1 >> s2;

	int hash[2] = { 0, 0 };

	unordered_map<char, char> opp;
	opp['W'] = 'E', opp['E'] = 'W', opp['N'] = 'S', opp['S'] = 'N';

	int p = 1;
	for (int i = n - 2; i >= 0; p *= base, --i) {
		hash[0] += opp[s1[i]] * p;
		hash[1] = base * hash[1] + s2[i];

		if (hash[0] == hash[1]) {
			cout << "NO";
			return 0;
		}

	}

	cout << "YES";
	return 0;

}
