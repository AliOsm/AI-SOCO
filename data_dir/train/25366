#include <bits/stdc++.h>
using namespace std;

vector<int> want[200005];
int pre[200005];
int buy[200005];

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin >> t; while (t--) {
		int n; cin >> n;
		multiset<int> co;
		for (int i = 0; i < n; ++i) {
			int m, p; cin >> m >> p;
			want[m].push_back(p);
		}
		for (int i = 1; i <= n; ++i) pre[i] = pre[i - 1] + want[i - 1].size();


		int have = 0;
		long long an = 0;
		for (int i = n; i >= 0; --i)  {
			for (int j : want[i]) co.insert(j);
			if (pre[i] + have >= i) {
				// cout << "i = " << i << " free" << endl;
			} else {
				while (pre[i] + have < i) {
					++have;
					an += *co.begin();
					co.erase(co.begin());
				}
			}
		}
		
		cout << an << endl;

		for (int i = 0; i <= n; ++i) want[i].clear();
	}
}
