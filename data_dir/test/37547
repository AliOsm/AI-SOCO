#include <bits/stdc++.h>
#define endl '\n'
#define debug(X) cout << #X << " = " << X << endl
#define fori(i,b,e) for (int i = (b); i < (e); ++i)
#define mod(x,m) ((((x) % (m)) + (m)) % (m))
#define sq(x) (x) * (x)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int oo = 1e9;

ll root(ll x) {
	ll low = 1, high = 1000001;
	while (high - low > 1) {
		ll mid = (low + high) * 0.5;
		if (mid * mid * mid <= x) low = mid;
		else high = mid;
	}
	return low;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n; cin >> n;
	while (n--) {
		ll a, b; cin >> a >> b;
		ll x = root(a*b);
		cout << (x * x * x == a * b && a % x == 0 && b % x == 0 ? "Yes" : "No") << endl;
	}
	return 0;
}