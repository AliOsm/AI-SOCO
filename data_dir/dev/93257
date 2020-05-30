#include <bits/stdc++.h>
#define endl '\n'
#define debug(X) cout << #X << " = " << X << endl
#define fori(i,b,e) for (int i = (b); i < (e); ++i)
#define mod(x,m) ((((x) % (m)) + (m)) % (m))
#define sq(x) (x) * (x)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int oo = 1e9;

ll pt10[20];

ll f(vi &v) {
	ll ans = 0, exp = 0;
	for (int i = 9; i >= 0; i--)
		for (int j = 0; j < v[i]; j++)
			ans += i * pt10[exp++];
	return ans;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	pt10[0] = 1;
	fori(i, 1, 19)
		pt10[i] = 10 * pt10[i - 1];

	ll a, b; cin >> a >> b;

	vi cnt(10);
	string sa = to_string(a);
	int n = sa.size();
	for (char c : sa)
		cnt[c - '0']++;

	ll ans = 0;
	for (int i = n - 1; i >= 0; i--) {
		int d = 9;
		while (true) {
			if (cnt[d]) {
				cnt[d]--;
				if (ans + d * pt10[i] + f(cnt) <= b)
					break;
				cnt[d]++;
			}
			d--;
		}
		ans += d * pt10[i];
	}

	cout << ans << endl;

	return 0;
}