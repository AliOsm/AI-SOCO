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
map<int,int> pos;
map<int,int> ans;
map<int,int> before;

int main() {
    ios_base::sync_with_stdio(false);
    int n; cin >> n;
    int last = 0;
    int best = 0;

    for(int i = 1; i <= n; i++) {
        int x; cin >> x;
        pos[x] = i;
        if(pos.count(x-1)) ans[i] = ans[pos[x-1]]+1, before[i] = pos[x-1];
        else ans[i] = 1;
        if(ans[i] > best) best = ans[i], last = i;
    }

    cout << best << endl;
    vector<int> ans;
    while(ans.size() < best) {
        ans.pb(last);
        last = before[last];
    }
    sort(ans.begin(),ans.end());
    for(auto x : ans) cout << x << " ";
    cout << endl;

    return 0;
}

