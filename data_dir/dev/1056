#include <bits/stdc++.h>
using namespace std;

int n, a, b, arr[25], ans;
bool ok = 1;
int main(){
	scanf("%d%d%d", &n, &a, &b);
	for(int i = 0; i < n; ++i){
		scanf("%d", arr + i);
	}

	for(int i = 0; i < n / 2; ++i){
		if(arr[i] == 2 && arr[n - i - 1] == 2){
			ans += min(a, b) * 2;
		}
		else if((arr[i] == 0 && arr[n - i - 1] == 2) || (arr[i] == 2 && arr[n - i - 1] == 0) ){
			ans += a;
		}
		else if((arr[i] == 1 && arr[n - i - 1] == 2) || (arr[i] == 2 && arr[n - i - 1] == 1) ){
			ans += b;
		}
		else if(arr[i] != arr[n - i - 1]){
			ok = 0;
			break;
		}
	}
	if(n & 1)
	if(arr[n / 2] == 2){
		ans += min(a, b);
	}
	if(ok)
		printf("%d", ans);
	else
		printf("%d", -1);
}
