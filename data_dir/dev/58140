#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
#define ld long double
using namespace std;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;

int n;
string s, ss;
vector<pair<int, int> > res;
bool swap(int idx){
	if(s[idx] == ss[idx]) return 1;
	for(int i = idx + 1; i < n; i++){
		if(s[i] == s[idx]){
			swap(ss[idx], s[i]);
			res.push_back({i, idx});
			return 1;
		}
	}
	for(int i = idx + 1; i < n; i++){
		if(ss[i] == ss[idx]){
			swap(s[idx], ss[i]);
			res.push_back({idx, i});
			return 1;
		}
	}
	return 0;
}

void exchange(int idx){
	for(int i = idx + 1; i < n; i++){
		if(ss[i] == s[idx]){
			swap(ss[i], s[i]);
			res.push_back({i, i});
			return ;
		}
	}
	for(int i = idx + 1; i < n; i++){
		if(s[i] == ss[idx]){
			swap(ss[i], s[i]);
			res.push_back({i, i});
			return ;
		}
	}
}

int main(){
	fast;
	int t;
	cin >> t;
	while(t--){
		cin >> n;
		
		cin >> s >> ss;
		string ans = "Yes";
		for(int i = 0; i < n; i++){
			if(swap(i)) continue;
			exchange(i);
			if(swap(i)) continue;
			ans = "No";
			break;
		}
		cout << ans << "\n";
		if(ans == "Yes"){
			cout << res.size() << "\n";
			for(auto i: res){
				cout << i.first + 1 << " " << i.second + 1 << "\n";
			}
		}
		res.clear();
	}
	
	return 0;
}
