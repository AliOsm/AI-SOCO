/*
Yea, those will be the days that I will be missing
	When I’m old and when I’m gray and when I stop working
I hope that I can say
	When all my days are done
That I had my fun!!!!!!!
*/
#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
#define ld long double
using namespace std;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;


int main(){
	fast;
	int n;
	cin >> n;
	string s;
	cin >> s;
	string ans;
	int xr = 0;
	for(int i = 0; i < n; i++){
		if(xr == 0){
			ans += s[i];
			xr ^= 1;
		}
		else{
			if(ans.back() == s[i]) continue;
			ans += s[i];
			xr ^= 1;
		}
	}
	if(ans.size() % 2) ans.pop_back();
	cout << (int)s.size() - (int)ans.size() << "\n";
	cout << ans;
	
	return 0;
}

