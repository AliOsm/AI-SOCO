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
	int ct = 0, ct1 = 0;
	for(auto i: s){
		if(i == '0') ct++;
		else ct1++;
	}
	if(ct != ct1){
		cout << 1 << "\n" << s;
		return 0;
	}
	cout << 2 << "\n";
	char ch = s.back();
	s.pop_back();
	cout << s << " " << ch;
	
	return 0;
}
