#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back

using namespace std;

typedef long long ll;

ll n, freq[80];
string s;
ll ans;
vector<pair<string,string> > xxx;
vector<string> jaw;

bool can(ll x){
	ll satunya = n/x;
	ll pasangan;
	if (satunya % 2 == 1) {
		pasangan = (satunya-1)/2;
		pasangan *= x;
		ll sisa = 0;
		for (int i = 0 ; i < 62; i++) {
			if (freq[i] > 0){
				if (freq[i]%2 == 0) {
					ll bil = (freq[i]/2);
					if (pasangan >= bil) {
						pasangan -= bil;
					}
					else {
						sisa += (bil-pasangan)*2;
						pasangan = 0;
					}
				}
				else {
					ll bil = (freq[i]-1)/2;
					if (pasangan >= bil) {
						pasangan -= bil;
						sisa++;
					}
					else {
						sisa++;
						sisa += (bil-pasangan)*2;
						pasangan = 0;
					}
				}
			}
		}
		if (pasangan == 0 && sisa == x) return true;
		return false;
	}
	else {
		pasangan = satunya/2; pasangan *= x;
		for (int i = 0 ; i < 62; i++) {
			if (freq[i] > 0) {
				if (freq[i]%2 == 1) return false;
				else pasangan -= freq[i]/2;
			}
		}
		if (pasangan == 0) return true;
		return false;
	}
}

char ub(int x){
	if (x <= 25) return char(x + 'a');
	else if (x <= 51) return char(x - 26 + 'A');
	else return char(x - 52 + '0');
}

void backtrack(){
	ll satunya = n/ans;
	vector<int> satu, dua;
	for (int i = 0; i < 62; i++) {
		if (freq[i]%2 == 0) {
			for (int j = 0 ; j < freq[i]; j++) dua.pb(i);
		}
		else {
			satu.pb(i);
			for (int j = 0 ; j < (freq[i]-1); j++) dua.pb(i);
		}
	}
	char ans[400005];
	for (int i = 0 ; i < s.size(); i++) ans[i] = '.';
	if (satunya % 2 == 1) {
		int now = (satunya-1)/2;
		int idx1 = 0;
		int idx2 = 0;
		while (now < s.size()) {
			if (idx1 < satu.size()) {
				ans[now] = ub(satu[idx1]);
				idx1++;
			}
			else if (idx1 == satu.size() || satu.size() == 0){
				ans[now] = ub(dua[idx2]);
				idx2++;
			}
			now += satunya;
		}
		now = 0;
		int noww = satunya-1-now;
		while (now < s.size()) {
			if (now == noww) {
				now += ((satunya-1)/2) + 1;
				noww = now + satunya-1;
				continue;
			}
			else {
				ans[now] = ub(dua[idx2]);
				idx2++;
				ans[noww] = ub(dua[idx2]);
				idx2++;
				now++; noww--;
			}
		}
	}
	else {
		int idx2 = 0;
		int now = 0;
		int noww = satunya-1-now;
		while (now < s.size()) {
			if (now > noww) {
				now--;
				now += (satunya/2)+1;
				noww = now + satunya-1;
				continue;
			}
			else {
				ans[now] = ub(dua[idx2]);
				idx2++;
				ans[noww] = ub(dua[idx2]);
				idx2++;
				now++; noww--;
			}
		}
	}
	int cot = 0;
	for (int i = 0 ; i < s.size(); i++) {
		if (cot == satunya) {
			cot = 0;
			cout << " ";
		}
		cout << ans[i];
		cot++;
	}
	cout << '\n';
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n >> s;
	for (int i = 0 ; i < n; i++){
		if (s[i] >= 'a' && s[i] <= 'z') {
			freq[s[i]-'a']++;
		}
		else if (s[i]  >= 'A' && s[i] <= 'Z') {
			freq[s[i]-'A'+26]++;
		}
		else freq[s[i]-'0'+52]++;
	}
	ans = (ll)1e9;
	for (ll i = 1; i <= (int)sqrt(n); i++) {
		if (n%i == 0) {
			ll j = n/i;
			if (can(i)) ans = min(ans, i);
			if (can(j)) ans = min(ans, j);
		}
	}
	cout << ans << '\n';
	backtrack();
	return 0;
}