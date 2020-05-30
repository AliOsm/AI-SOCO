 //used editorial
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
#define ull unsigned long long int
#define ld long double
using namespace std;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;

ull n, h;
ull calc(ull mid){
	ull hi = min(h, mid);
	ull total = mid * mid - (hi * (hi - 1) / 2);
	return total;
}
	
int main(){
	fast;
	cin >> n >> h;
	ull lo = 0, hi = 1e10 + 1;
	while(hi - lo > 1){
		ull mid = hi + lo >> 1LL;
		if(calc(mid) <= n)  lo = mid;
		else hi = mid;
	}
	ull tt = min(h, lo);
	ull total  = lo * lo - (tt * (tt - 1) / 2); 
	ull ans = 2 * lo - 1 - (tt - 1);
	n -= total;
	ans += (n + lo - 1) / lo;
	cout << ans;
	
	return 0;
}
