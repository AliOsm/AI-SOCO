#include <bits/stdc++.h>
using namespace std;

int jam,menit;
int n,i,j;
char ch;

void cetak(int n){
	if (n < 10) cout << "0" << n ;
	else cout << n ;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> jam >> ch >> menit;
	//cout << jam << " " << menit;
	cin >> n;
	for (i = 1 ; i <= n ; i++) {
		menit++;
		if (menit == 60) {
			menit = 0;
			jam++;
			if (jam == 24) jam = 0;
		}
	}
	cetak(jam); cout << ':'; cetak(menit); cout << '\n';
	return 0;
}