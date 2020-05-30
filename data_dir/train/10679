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
const int T = 2e3 + 10;
ll v[T];

int main() {
    ios::sync_with_stdio(false);
    ll n; cin >> n;
    for(int i = 0; i < n; i++)
        cin >> v[i];
    cout << n+1 << endl;
    ll acum = 1e5 + 10;
    cout << 1 << " " << n << " " << acum << endl;
    for(int i = 0; i < n; i++) 
        cout << 2 << " " << i+1 << " " << (v[i] + acum) - i <<  endl;

    return 0;
}

