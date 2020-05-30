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

const int T = 5e5 + 10;
int v[T];
int n;
string s;

ll karatsubaP() {
    ll diff = 0;
    ll best = 0;
    for(int i = 0; i < n; i++) {
        if(s[i] == 'A') diff += v[i];
        else diff -= v[i];
        if(diff > best) best = diff;
    }
    diff = 0;
    for(int i = n-1; i >= 0; i--) {
        if(s[i] == 'A') diff += v[i];
        else diff -= v[i];
        if(diff > best) best = diff;
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n;
    for(int i = 0; i < n; i++) cin >> v[i];
    cin >> s;
    ll ans = 0;
    for(int i = 0; i < n; i++) 
        if(s[i] == 'B') ans += v[i];
    ans += karatsubaP();
    cout << ans << endl;
    return 0;
}

