//besmellah
#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	long long n, p, w, d;
	cin >> n >> p >> w >> d;
	vector <long long> X;
	for (long long i = 0; i < d; i ++){
		if (i * (w % d) % d == p % d){
			X.push_back(i);
		}
	}
	if (n * w < p){
		cout << -1;
		return 0;
	}
	if (X.size() == 0){
		cout << -1;
		return 0;
	}
	long long ans = X[0];
	long long y = p / w;
	for (auto x: X){
		if (y % d < x){
			ans = max(ans, (y / d - 1) * d + x);
		}
		else
			ans = max(ans, (y / d) * d + x);
	}
	long long x = ans;
	y = (p - x * w) / d;
	long long z = (n - (x + y));
	if (p < w){
		x = 0;
		y = p / d;
		z = n - y;
		if (y * d != p){
			cout << -1;
			return 0;
		}
	}
	if (z >= 0){
		cout << x << ' ' << y << ' ' << z;
	}
	else
		cout << -1;
}
