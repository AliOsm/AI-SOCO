#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

ll n,i,j,maks;
ll arr[100005];
ll ans[100005];
ll urutan[100005];
set<pll> himp;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n;
	for (i = 1 ; i <= n ; i++) {
		ll x;
		cin >> x;
		arr[i] = arr[i-1] + x;
	}
	for (i = 1 ; i <= n ; i++) cin >> urutan[i];
	for (i = n ; i >= 1 ; i--) {
		if (i == n) {
			ans[i] = 0;
			maks = arr[urutan[i]] - arr[urutan[i]-1];
			himp.insert({urutan[i], urutan[i]});
			//cout << i << " " << maks << endl;
		}
		else {
			set<pll>::iterator it,tt;
			it = himp.lower_bound({urutan[i],urutan[i]});
			tt = it;
			ll xx = it->fi;
			ll yy = it->se;
			ans[i] = maks;
			if (it == himp.end()){
				//cout << "masuk sini " << 1 << '\n';
				it--;
				ll xxx = it->fi;
				ll yyy = it->se;
				if (yyy + 1 == urutan[i]) {
					himp.erase(it);
					himp.insert({xxx,urutan[i]});
					maks = max(maks, arr[urutan[i]] - arr[xxx-1]);
				}
				else {						
					himp.insert({urutan[i],urutan[i]});
					maks = max(maks, arr[urutan[i]] - arr[urutan[i]-1]);
				}
			}
			else if (it == himp.begin()){
				//cout << "masuk sini " << 2 << '\n';
				if (xx == urutan[i] + 1) {
					himp.erase(it);
					himp.insert({urutan[i],yy});
					maks = max(maks, arr[yy] - arr[urutan[i]-1]);
				}
				else {
					himp.insert({urutan[i],urutan[i]});
					maks = max(maks, arr[urutan[i]] - arr[urutan[i]-1]);
				}
			}
			else {	
				//cout << "masuk sini " << 3 << '\n';
				it--;
				ll xxx = it -> fi;
				ll yyy = it -> se;
				//cout << xxx << " " << yyy << '\n';
				if (yyy + 1 == urutan[i] && urutan[i] + 1 == xx) {
					himp.erase(it);
					himp.erase(tt);
					himp.insert({xxx,yy});
					maks = max(maks, arr[yy] - arr[xxx-1]);
				}
				else if (urutan[i] + 1 == xx) {
					it++;
					himp.erase(it);
					himp.insert({urutan[i],yy});
					maks = max(maks, arr[yy] - arr[urutan[i]-1]);
				}
				else if (yyy + 1 == urutan[i]) {
					himp.erase(it);
					himp.insert({xxx,urutan[i]});
					maks = max(maks,arr[urutan[i]] - arr[xxx-1]);
				}
				else {
					himp.insert({urutan[i],urutan[i]});
					maks = max(maks, arr[urutan[i]]-arr[urutan[i]-1]);
				}
			}
			//cout << i << " " << maks << endl;
		}
	}
	for (i = 1; i <= n ; i++) {
		cout << ans[i] << '\n';
	}
	return 0;
}