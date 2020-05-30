#include<bits/stdc++.h>
using namespace std;

string rot(string &p, int type) {
	vector<int> mp;
	switch(type) {
		case 0:
			mp={4,0,5,1};
			break;
		case 1:
			mp={2,0,3,1};
			break;
		default:
			mp={4,2,5,3};
	}
	string q=p;
	int n=mp.size();
	for (int i=0; i<n; i++)
		q[mp[(i+1)%n]]=p[mp[i]];
	return q;
}

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	string p; cin>>p;
	sort(p.begin(), p.end());
	set<string> vis;
	int ret=0;
	do {
		if(vis.find(p)!=vis.end())
			continue;
		ret++;
		queue<string> q;
		q.push(p); vis.insert(p);
		while(!q.empty()) {
			string cur=q.front(); q.pop();
			for (int i=0; i<3; i++) {
				string nxt=rot(cur,i);
				if(vis.find(nxt)!=vis.end())
					continue;
				vis.insert(nxt);
				q.push(nxt);
			}
		}
	} while(next_permutation(p.begin(), p.end()));
	cout << ret << endl;
	return 0;
}
