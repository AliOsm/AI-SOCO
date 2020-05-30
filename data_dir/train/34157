#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	string s; cin>>s;
	int l=s.size();
	int n=(l+19)/20, m=(l+ n-1)/n;
	cout<<n<<" "<<m<<endl;
	int p=0, t;
	for (int i=0; i<n; i++) {
		if(i<n*m-l) t=m-1;
		else t=m;
		cout<<s.substr(p,t);
		if(t!=m) cout<<"*";
		cout<<endl;
		p+=t;
	}
	return 0;
}
