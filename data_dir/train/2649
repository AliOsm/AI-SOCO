#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define eb emplace_back
#define mk make_pair
#define fi first
#define se second

typedef pair<int,int> ii;
typedef long long ll;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const int T = 1e7;
const ll lim = 1e10 + 3;
vector<ll>two;
ll sum[T];

void pre() {
	two.pb(1);
	sum[0] = 1;
	int j = 0;
	for(ll i = 2; i <= lim; i *= 2) {
		two.pb(i);
		sum[++j] = sum[j-1] + i;
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	pre();
	int tc; cin >> tc;
	while(tc--) {
		ll n; cin >> n;
		ll tot = (n*(n+1))/2;
		int pos = lower_bound(two.begin(), two.end(), n) - two.begin();
		cout << tot - (n != two[pos]? 2*sum[pos-1] : 2*sum[pos]) << endl;
	}
	return 0;
}

