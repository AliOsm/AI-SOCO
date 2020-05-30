#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll> s;
ll x;

double f(ll mid) {
	return (s[mid]+x)/double(mid+1);
}

double t_search() {
	double ans=1e18;
	ll lo=0,hi=s.size()-2;
	for (int it=0; it<20; it++) {
		ll mid1 = lo+(hi-lo)/3;
		ll mid2 = hi-(hi-lo)/3;
		if (f(mid1)<=ans) ans=f(mid1);
		if (f(mid2)<=ans) ans=f(mid2);
		if (f(mid1)>=f(mid2)) lo=mid1;
		else hi=mid2;
	}
	for (int i=-1; i<=1; i++)
		for (int cur : {lo+i, hi+i})
			if(0<=cur&&cur<s.size()) ans=min(ans,f(cur));
	return x - ans;
}

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int q; cin>>q;
	s.push_back(0);
	while(q--) {
		int op; cin>>op;
		if(op==1) {
			cin>>x;
			s.push_back(s.back()+x);
		}
		else {
			cout << setprecision(10) << fixed << t_search() << endl;
		}
	}
	return 0;
}
