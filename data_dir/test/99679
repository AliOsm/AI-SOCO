#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;
const int T = 110;
int v[T];

int main() {
    ios::sync_with_stdio(false);
    int n; cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> v[i];

    int cust = 0;
    for(int j = 1; j <= n; j++) 
        cust += ((j-1)*v[j]*2)*2;
    cout << cust << endl;
    return 0;
}

