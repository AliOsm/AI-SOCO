#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,x; cin>>n;
	vector<int> p(n);
	p[0]=0;
	int mx=0;
	for (int i=1; i<n; i++)
		cin>>x,
		p[i]=x+p[i-1],
		mx=max(mx,p[i]);
	int add=n-mx;
	for (int i=0; i<n; i++)
		p[i]+=add;
	set<int> st(p.begin(), p.end());
	if(st.size()!=n) {
		cout << -1 << endl;
		return 0;
	}
	for (int i=0; i<n; i++)
		if(p[i]<1) {
			cout << -1 << endl;
			return 0;
		}

	for (auto it : p)
		cout << it << " ";
	cout << endl;
	return 0;
}
