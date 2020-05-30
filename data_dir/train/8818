#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll n,k,i,j;
ll arr[100005];
ll satu,dua;

bool bisa(ll x){
	ll depan,z,belakang;
	depan = n-1;
	belakang = 0;
	for (z = 0 ; z < satu ; z++) {
		if (arr[depan] > x) return false;
		else depan--;
	}
	for (z = 0; z < dua; z++) {
		if (arr[depan]+arr[belakang] > x) return false;
		else {
			depan--;
			belakang++;
		}
	}
	return true;
}

ll binser(ll l,ll r){
	ll ret;
	while (l<=r) {
		ll mid = (l+r)/2;
		if (bisa(mid)) {
			ret = mid;
			r = mid-1;
		}
		else l = mid+1;
	}
	return ret;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n >> k;
	if (n >= k) {
		satu = 2*k-n; dua = n-k;
	}
	else {
		dua = 0; satu = n;
	}
	for (i = 0 ; i < n ; i++)
		cin >> arr[i];
	cout << binser(1,1000000000) << '\n';
	return 0;
}