#include <bits/stdc++.h>
using namespace std;

#define fr(i,n) _back
#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const int T = 5e3 + 3;
int freq[T];

int main() {
    ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    while(tc--) {
        int n; cin >> n;
        vector<int> v(n);
        bool ans = 0;

        for(int i = 0; i < n; i++) {
            cin >> v[i];
            freq[v[i]]++;
            ans |= (freq[v[i]] > 2 or (freq[v[i]] == 2 and v[i-1] != v[i]));
        }

        for(int i = 0; i < n; i++) freq[v[i]] = 0;
        cout << (ans? "YES":"NO") << endl;
    }
    return 0;
}

