#include <bits/stdc++.h>

#define fi first
#define se second
#define pb push_back

using namespace std;

typedef pair<int,int> ii;

string s;
vector<ii> arr;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> s;
	int i = 0;
	int j = s.find("bear", i);
	while (j >= 0 && j < s.size()) {
		arr.pb({j, j + 3});
		i = j + 1;
		j = s.find("bear", i);
	}
	int ans = 0;
	for (int i = 0 ; i < s.size(); i++) {
		int lo = 0;
		int hi = (int)arr.size()-1;
		int mulai = -1;
		while (lo <= hi) {
			int mid = (lo + hi) >> 1;
			if (arr[mid].fi > i) {
				mulai = mid;
				hi = mid - 1;
			}
			else if (arr[mid].fi == i) {
				mulai = mid;
				break;
			}
			else {
				lo = mid + 1;
			}
		}
		if (mulai != -1) {
			int ujung = (int)s.size()-1;
			ans += ujung - (arr[mulai].se) + 1;
		}
	}
	cout << ans << '\n';
	return 0;
}