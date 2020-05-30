#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define N 100005
#define ll long long 

int a[N];

int main(){
	ios::sync_with_stdio(false);
	//freopen("input.txt", "r", stdin);
	int i, n, d; cin>>n>>d;
	for(i=0; i<n; i++){
		cin>>a[i];
	}
	int val, ans = 2;
	for(i=0; i<n-1; i++){
		val = a[i+1] - a[i] - d - d + 1;
		if(val > 0){
			if(val == 1){
				ans++;
			}
			else{
				ans += 2;
			}
		}
	}
	cout<<ans;
	return 0;
}