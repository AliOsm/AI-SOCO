#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
#define ld long double
using namespace std;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;

multiset <ll> st;
int main(){
	fast;
	ll n, m, k, x;
	cin >> n >> m >> k;
	for(int i = 0; i < n; i++){
		cin >> x;
		st.insert(x);
	}
	auto it = st.end();
	it--;
	ll mx1 = *it;
	it--;
	ll mx2 = *it;
	ll ct = 0, ct1 = 0, sum = 0;
	x = 0;
	ct = m / (k + 1);
	sum += (ct * k) * mx1;
	sum += ct * mx2;
 	sum += (m % (k + 1)) * mx1;
 	cout << sum;
	
	return 0;
}

