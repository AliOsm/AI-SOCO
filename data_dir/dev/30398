#include <bits/stdc++.h>

#define endl '\n'
#define ll long long int
#define let(x, a) __typeof(a) x(a)
#define all(a) (a).begin(), (a).end()
#define present(c, x) ((c).find(x) != (c).end())
#define tr(v, it) for (let(it, v.begin()); it != v.end(); it++)
#define rtr(v, it) for (let(it, v.rbegin()); it != v.rend(); it++)

#define trace1(x)					cerr << #x << ": " << x << endl;
#define trace2(x, y)				cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)				cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)			cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)		cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f)	cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int tt,R,P,S,n,w;
	string s;
	cin>>tt;
	vector<char> t;
	while(tt--) {
		cin>>n;
		cin>>R>>P>>S;
		cin>>s;
		t.assign(n,'.');
		w=(n%2 == 0) ? n/2 : n/2 + 1;
		for(int i=0;i<n && w>0;i++) {
			if(s[i]=='R') {
				if(P>0) {
					t[i]='P';
					P--;
					w--;
				}
			} else if(s[i]=='P') {
				if(S>0) {
					t[i]='S';
					S--;
					w--;
				}
			} else {
				if(R>0) {
					t[i]='R';
					R--;
					w--;
				}
			}
		}
		if(w>0) cout<<"NO"<<endl;
		else {
			cout<<"YES"<<endl;
			for(int i=0;i<n;i++) {
				if(t[i]=='.') {
					if(R>0) {
						t[i]='R';
						R--;
					} else if(P>0) {
						t[i]='P';
						P--;
					} else {
						t[i]='S';
						S--;
					}
				}
				cout<<t[i];
			}
			cout<<endl;
		}
	}
	return 0;
}