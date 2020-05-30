 /*
    __                      _    _            __                 __
   / /_/\__        __ _    | | _| | __     _  \ \       __/\__  / /
  / /\    /       / _` |   | |/ / |/ /    (_)  | |      \    / / / 
 / / /_  _\      | (_| |   |   <|   <      _   | |      /_  _\/ /  
/_/    \/         \__,_|___|_|\_\_|\_\    (_)  | |        \/ /_/   
                      |_____|                 /_/                  

*/
#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
#define ld long double
using namespace std;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;

string ans;
vector<pair<string, ll> > h[200];
char out[500];
bool checkpre(string s){
	for(int i = 0; i < (int)s.size(); i++){
		if(ans[i]  != s[i]) return 0;
	}
	return 1;
}
bool checksuff(string s){
	reverse(ans.begin(), ans.end());
	reverse(s.begin(), s.end());
	for(int i = 0; i < (int)s.size(); i++){
		if(ans[i] != s[i]){
			reverse(ans.begin(), ans.end());
			return 0;
		}
	}
	reverse(ans.begin(), ans.end());
	return 1;
}

int main(){
	fast;
	ll n, flag = 0;
	cin >> n;
	for(int i = 0; i < (2 * n - 2); i++){
		string t;
		cin >> t;
		h[(int)t.size()].push_back({t, i});
	}

	ans =  h[n - 1][0].first + h[n - 1][1].first.back();
	//cout << ans << " ";
	for(int i = 1; i <= n - 1; i++){
		//cout << h[i][0].first << " " << h[i][1].first << "\n";
		if(checksuff(h[i][0].first) && checkpre(h[i][1].first)){
			//cout << "yo1\n";
			out[h[i][0].second] = 'S';
			out[h[i][1].second] = 'P';
			//cout << h[i][0].second << " " << h[i][1].second << "\n";
		}
		else if (checksuff(h[i][1].first) && checkpre(h[i][0].first)){
			//cout << "yo2\n";
			out[h[i][0].second] = 'P';
			out[h[i][1].second] = 'S';
			//cout << h[i][0].second << " " << h[i][1].second << "\n";
		}
		else{
			flag = 1;
			break;
		}
	}
	if(!flag){
		for(int i = 0; i < 2 * n - 2 ; i++){
			cout << out[i];
		}
		return 0;
	}
	flag = 0;
	ans =  h[n - 1][1].first + h[n - 1][0].first.back();
	for(int i = 1; i <= n - 1; i++){
		if(checksuff(h[i][0].first) && checkpre(h[i][1].first)){
			out[h[i][0].second] = 'S';
			out[h[i][1].second] = 'P';
		}
		else if (checksuff(h[i][1].first) && checkpre(h[i][0].first)){
			out[h[i][0].second] = 'P';
			out[h[i][1].second] = 'S';
		}
		else{
			flag = 1;
			break;
		}
	}
	if(!flag){
		for(int i = 0; i < 2 * n - 2 ; i++){
			cout << out[i];
		}
		return 0;
	}
	return 0;
}
