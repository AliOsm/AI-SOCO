#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
#endif
	
	int n, k;
	cin >> n >> k;
	vector<pair<int, int>> a(n);
	for (int i = 0; i < n; ++i) {
		cin >> a[i].first;
		a[i].second = i;
	}
	
	sort(a.rbegin(), a.rend());
	queue<int> q;
	for (int i = 0; i < n; ++i) {
		q.push(a[i].second);
	}
	
	set<int> idx;
	for (int i = 0; i < n; ++i) {
		idx.insert(i);
	}
	string ans(n, '0');
	int who = 0;
	while (!idx.empty()) {
		while (!idx.count(q.front())) {
			q.pop();
		}
		int pos = q.front();
		q.pop();
		
		vector<int> add;
		auto it = idx.find(pos);
		for (int i = 0; i <= k; ++i) {
			add.push_back(*it);
			if (it == idx.begin()) break;
			--it;
		}
		it = next(idx.find(pos));
		for (int i = 0; i < k; ++i) {
			if (it == idx.end()) break;
			add.push_back(*it);
			++it;
		}
		for (auto it : add) {
			idx.erase(it);
			ans[it] = '1' + who;
		}
		who ^= 1;
	}
	
	cout << ans << endl;
	
	return 0;
}