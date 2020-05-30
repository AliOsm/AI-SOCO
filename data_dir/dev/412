#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define N 150005
#define M 30
#define ll long long 
#define ld long double
#define pb push_back
#define ff first
#define ss second

int a[N], f[N] = {0};

int main(){
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int n, i, x, cnt, ans;
	cin>>n;
	for(i=0; i<n; i++){
		cin>>a[i];
	}
	sort(a, a+n);
	f[0] = 1;
	ans = 0;
	for(i=0; i<n; i++){
		if(f[a[i] - 1] == 0){
			ans++;
			f[a[i] - 1]++;
		}
		else if(f[a[i]] == 0){
			ans++;
			f[a[i]]++;
		}
		else if(f[a[i] + 1] == 0){
			ans++;
			f[a[i] + 1]++;
		}
	}
	cout<<ans;
	return 0;
}