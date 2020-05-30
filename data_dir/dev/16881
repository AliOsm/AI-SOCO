#include <bits/stdc++.h>
using namespace std;

vector<int> ans;
int n,m,i,j;

int gcd(int a,int b){
	return (b==0 ? a : gcd(b,a%b));
}

int main(){
	cin >> n;
	int arr[1005];
	for (i = 0 ; i < n ; i++) {
		cin >> arr[i];
	}
	for (i = 0 ; i < n-1 ; i++) {
		if (gcd(arr[i],arr[i+1])!=1) {
			ans.push_back(i);
		}
	}
	cout << ans.size() << '\n';
	for (i = 0 ; i < n ; i++) {
		cout << arr[i] << " ";
		if (j < ans.size() && i == ans[j]) {
			cout << 1 << " ";
			j++;
		}
	}
	cout << '\n';
}