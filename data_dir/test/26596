#include <bits/stdc++.h>
using namespace std;

//Define Lists
#define fi first
#define se second
#define pb push_back
#define sz(x) (int)x.size() 
#define all(x) (x).begin(), (x).end()
#define OPTIMATION ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define inp() freopen("in.txt", "r", stdin);
#define out() freopen("out.txt", "w", stdout);
#define IO inp() out()

//typedef Lists
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;

//constant values
const double pi = acos(-1);
const LL MODPRIMA = (LL)1e9 + 7;
const LL MAXX = (LL)1e18;
const LL MINN = -(LL)1e18;
const double EPS = 1e-9;

//declare variables here
LL N, M, K;

int main(){
  OPTIMATION
  cin >> N >> M >> K;
  if (K > N-1 + M-1) cout << -1 << '\n';
  else {
  	LL ans = 0;
  	if (K <= N-1) {
  		ans = (N/(K+1))*M;
  	}
  	if (K <= M-1){
  		ans = max(ans, (M/(K+1))*N);
  	}

  	if (K > N-1){
  		ans = max(ans, (M/(K-(N-1)+1)));
  	}
  	if (K > M-1) {
  		ans = max(ans, (N/(K-(M-1)+1)));
  	}
  	cout << ans << '\n';
  }
  return 0;
}