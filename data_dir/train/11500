#include <bits/stdc++.h>
using namespace std;
 
#define pb push_back
#define eb emplace_back
#define mk make_pair
#define fi first
#define se second
#define cc(x)	cout << #x << " = " << x << endl
#define ok		cout << "ok" << endl
#define endl '\n'
 
typedef long long ll;
typedef pair<int,int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
 
const int T = 1e3 + 5;
int v[T];
 
int main() {
    ios_base::sync_with_stdio(false);
	int n, k;
	cin >> n >> k;
	int x;
 
	for(int i = 0; i < n; i++) {
		cin >> x;
		v[x]++;
	}
   
	int par = 0;
	int imp = 0;
 
	for(int i = 1; i <= k; i++) {
		if(!v[i]) continue;
		if(v[i] >= 2) {
			par += v[i]/2;
		}
		if(v[i]&1) imp++;
	}
 
	int tot = n/2 + (n&1);
	tot -= par;
 
	int ans = par*2;
	ans += min(tot,imp);
	
	cout << ans << endl;
    
    return 0;
}
