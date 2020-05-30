#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll n,a,b,c,d;
ll atas,bawah;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n >> a >> b >> c >> d;
	atas = n; bawah = 1;
	atas = min(atas,n+c-b);
	atas = min(atas,n+d-a);
	atas = min(atas,n+c+d-a-b);
	//cout << n+c-b << " " << n+d-a << " " << n+c+d-a-b << '\n';
	bawah = max(bawah,c-b+1);
	bawah = max(bawah,d-a+1);
	bawah = max(bawah,c+d-a-b+1);
	cout << (atas < bawah ? 0 : (atas-bawah+1)*n) << '\n';
	return 0;
}