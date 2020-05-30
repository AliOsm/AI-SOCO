#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define mkp make_pair
#define pii pair<int, int> 
#define pll pair<long long int, long long int>
#define sci(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define fi first
#define sc second
#define deb 0

string A[10000], B[10000];

int main()
{
	ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);

	int n, m, i, j, k;
	cin >> n >> m;
	if (n > m) {
		cout << "YES" << endl; return 0;
	} else if (n < m) {
		cout << "NO" << endl; return 0;
	}

	for (i = 0; i < n; ++i) cin >> A[i];
	for (i = 0; i < m; ++i) cin >> B[i];

	k = n;
	for (i = 0; i < n; ++i) {
		for (j = 0; j < m; ++j) {
			if (A[i] == B[j]) k--;
		}
	}
	k = n - k;
	if (k%2) cout << "YES" << endl;
	else cout << "NO" << endl;

	return 0;
}
