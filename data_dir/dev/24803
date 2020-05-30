#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define eb emplace_back
#define mk make_pair
#define fi first
#define se second
#define endl '\n'

typedef long long ll;
typedef pair<int,int> ii;
const int INF = 0x3f3f3f3f;

vector<int> u;
vector<int> p;

int main() {
    ios_base::sync_with_stdio(false);
	int a,b,c;
	cin >> a >> b >> c;
	int m; cin >> m;	
	string s;
	int x;
	ll tot = a+b+c;

	for(int i = 0; i < m; i++) {
		cin >> x >> s;
		if(s == "USB") u.pb(x);
		else p.pb(x);
	}

	sort(u.begin(), u.end());
	sort(p.begin(), p.end());

	int i = 0; int j = 0;
	ll ans = 0;

	while(i < u.size() and a) {
		ans += u[i++];
		a--;
	}
	
	while(j < p.size() and b) {
		ans += p[j++];
		b--;
	}
	
	while((i < u.size() or j < p.size()) and c) {

		if(i < u.size() and j < p.size()) {
			if(u[i] <= p[j]) ans += u[i++];
			else ans += p[j++];
			c--;
		} 
		else if(i < u.size()) ans += u[i++], c--;
		else if(j < p.size()) ans += p[j++], c--;

	}
    
	cout << tot - (a+b+c) << " " << ans << endl;

    return 0;
}

