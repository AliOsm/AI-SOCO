#include <bits/stdc++.h> 
using namespace std;
typedef long long ll;

const int N = 150005;
int t[N];
int n, q, k;
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	cin >> n >> k >> q;
	for (int i = 0; i < n; ++i)
		cin >> t[i];
	set<int> online;
	while (q--) {
		int tmp, id;
		cin >> tmp >> id;
		--id ;
		if (tmp == 1) {
			online.insert(t[id]);
			if (online.size() > k) online.erase(online.begin());
		}
		else {
			cout << (online.count(t[id]) ? "YES\n" : "NO\n");
		}
	}
}
