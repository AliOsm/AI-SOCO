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

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	set<int> dict;
	for (int k = 1; k * (k + 1) < 2e9; k++)
		dict.insert((k * (k + 1)) >> 1);
	int n;
	while (cin >> n) {
		int ans = 0;
		for (int d : dict) {
			if (d > n) break;
			ans |= (dict.find(n - d) != dict.end());
		}
		cout << (ans ? "YES" : "NO") << endl;
	}
	return 0;
}