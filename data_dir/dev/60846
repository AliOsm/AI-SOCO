#include <bits/stdc++.h>
using namespace std;

int n,m,i,j;
string s;
int udah[30];

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n >> s;
	int ans = 0;
	if (n > 26) {
		cout << -1 << '\n';
		return 0;
	}
	else {
		for (i = 0 ; i < s.size(); i++){
			udah[(int)s[i]-'a']++;
		}
		for (i = 0 ; i < 26 ; i++) {
			if (udah[i] > 1) ans += udah[i]-1;
		}
		cout << ans << '\n';
	}
	return 0;
}