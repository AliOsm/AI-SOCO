#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n; cin>>n;
	string s,t; cin>>s>>t;
	map<char,queue<int>> left, right;
	for (int i=0; i<n; i++)
		left[s[i]].push(i+1),
		right[t[i]].push(i+1);
	vector<ii> ret;
	for (char ch='a'; ch<='z'; ch++) {
		while(!left[ch].empty()&&!right[ch].empty()) {
			ret.push_back({left[ch].front(), right[ch].front()});
			left[ch].pop(); right[ch].pop();
		}
	}
	for (char ch='a'; ch<='z'; ch++) {
		while(!left[ch].empty()&&!right['?'].empty()) {
			ret.push_back({left[ch].front(), right['?'].front()});
			left[ch].pop(); right['?'].pop();
		}
	}

	for (char ch='a'; ch<='z'; ch++) {
		while(!left['?'].empty()&&!right[ch].empty()) {
			ret.push_back({left['?'].front(), right[ch].front()});
			left['?'].pop(); right[ch].pop();
		}
	}

	while(!left['?'].empty()&&!right['?'].empty()) {
		ret.push_back({left['?'].front(), right['?'].front()});
		left['?'].pop(); right['?'].pop();
	}

	cout << ret.size() << endl;
	for (auto it : ret)
		cout << it.first << " " << it.second << endl;
	return 0;
}
