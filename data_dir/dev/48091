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

const int oo = 1e9, mxn = 110;

int W[mxn], H[mxn];

bool check(int w1, int h1, int w2, int h2, int a, int b) { return w1 + w2 <= a && max(h1, h2) <= b; }

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n, a, b; cin >> n >> a >> b;
	fori(i, 0, n)
		cin >> W[i] >> H[i];
	int ans = 0;
	fori(i, 0, n) {
		fori(j, 0, i) {
			if (check(W[i], H[i], W[j], H[j], a, b) ||
					check(W[i], H[i], H[j], W[j], a, b) ||
					check(H[i], W[i], W[j], H[j], a, b) ||
					check(H[i], W[i], H[j], W[j], a, b) || 
					check(W[i], H[i], W[j], H[j], b, a) ||
					check(W[i], H[i], H[j], W[j], b, a) ||
					check(H[i], W[i], W[j], H[j], b, a) ||
					check(H[i], W[i], H[j], W[j], b, a))
				ans = max(ans, W[i] * H[i] + W[j] * H[j]);
		}
	}
	cout << ans << endl;
	return 0;
}