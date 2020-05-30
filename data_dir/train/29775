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

const int T = 1e5 + 4;
int v[T];
int n;

int main() {
    ios::sync_with_stdio(false);
    cin >> n;
    int mini = INF;

    for(int i = 0; i < n; i++) cin >> v[i], mini = min(mini,v[i]);

    int last = -1;
    int at = -1;
    int ans = INF;

    for(int i = 0; i < n; i++) { 
        if(v[i] == mini) {
            if(at == -1) at = i; 
            else {
                last = at;
                at = i;
                ans = min(ans, at-last);
            }
        }
    }

    cout << ans << endl;

    return 0;
}

