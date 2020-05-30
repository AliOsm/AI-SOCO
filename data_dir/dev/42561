#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int t; cin>>t;
	while(t--) {
		int n; cin>>n;
		string s; cin>>s;
		int a=0, b=0;
		for (int i=0; i<n; i++) {
			if(s[i]=='>') break;
			a++;
		}
		for (int i=n-1; i>=0; i--) {
			if(s[i]=='<') break;
			b++;
		}
		cout << min(a,b) << endl;
	}
	return 0;
}
