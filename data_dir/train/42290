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
const int T = 1e7+2;
bitset<T> crivo;
int freq[T];
int ans[T];

void init() {
    for(int i = 2; i < T; i++) {
        if(!crivo[i]) {
            for(int j = i; j < T; j += i) {
                crivo[j] = 1;
                if(freq[j]) ans[i] += freq[j];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int n; cin >> n;
    for(int i = 0; i < n; i++) {
        int x; cin >> x;
        freq[x]++;
    }

    init();

    for(int i = 1; i < T; i++) ans[i] += ans[i-1];
    int q; cin >> q;

    while(q--) {
        int l,r; cin >> l >> r;
        r = min(r,T-2);
        l = min(l,T-2);
        cout << ans[r] - ans[l-1] << endl;
    }

    return 0;
}

