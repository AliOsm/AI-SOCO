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
int n,d;
set<int> ans;
int v[T];

void check(int source) {
    int mini = INF;
    for(int i = 0; i < n; i++) mini = min(mini, abs(source - v[i]));
    if(mini == d) ans.insert(source);
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> d;
    for(int i = 0; i < n; i++) cin >> v[i];
    sort(v, v+n);
    for(int i = 0; i < n; i++) {
        check(v[i] + d);
        check(v[i] - d);
    }
    cout << ans.size() << endl;
    return 0;
}

