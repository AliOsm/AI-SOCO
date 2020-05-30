#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<ll,int> ii; 


int n;
ll s;
ii arr[100005], tmp[100005];

bool comp(ii a,ii b){
	return a.fi < b.fi;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n >> s;
	for (int i = 0 ; i < n ; i++) {
		cin >> arr[i].fi;
		arr[i].se = i + 1;
	}
	int kiri = 0, kanan = n;
	int ans = 0;
	ll res = 0;
	while (kiri <= kanan) {
		int mid = (kiri + kanan)/2;
		for (int i = 0 ; i < n ; i++) {
			tmp[i].se = i + 1;
			tmp[i].fi = arr[i].fi + (ll)mid * (ll)(i + 1);
		}
		sort(tmp, tmp + n, comp);
		ll tot = 0;
		for (int i = 0 ; i < mid; i++) {
			tot += tmp[i].fi;
		}
		if (tot <= s) {
			if (mid > ans) {
				ans = mid;
				res = tot;
			}
			else if (mid == ans) res = min(res, tot);
			kiri = mid + 1;
		}
		else kanan = mid - 1;
	}
	cout << ans << " " << res << '\n';
	return 0;
}