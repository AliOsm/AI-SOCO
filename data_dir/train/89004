#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

ll n,m,i,j;
ll x,y;
vector<pll> A;
map<pll,ll> mep;
map<ll,ll> frekx,freky;
vector<ll> arrx,arry;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n;
	for (i = 0 ; i < n ; i++) {
		cin >> x >> y;
		A.push_back(make_pair(x,y));
		mep[make_pair(x,y)]++;
		frekx[x]++; freky[y]++;
		if (frekx[x]==1) arrx.push_back(x);
		if (freky[y]==1) arry.push_back(y);
	}
	ll ans = 0;
	for (i = 0 ; i < arrx.size(); i++) {
		ans += (frekx[arrx[i]]*(frekx[arrx[i]]-1))/2;
	}
	for (i = 0 ; i < arry.size(); i++) {
		ans += (freky[arry[i]]*(freky[arry[i]]-1))/2;
	}
	for (i = 0 ; i < n ; i++) {
		if (mep[A[i]] > 1) {
			ans -= (mep[A[i]]*(mep[A[i]]-1))/2;
			mep[A[i]] = 0;
		}
	}
	cout << ans << '\n';
	return 0;
}