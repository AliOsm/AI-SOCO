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

 
int main() {
    ios_base::sync_with_stdio(false);
    int n; cin >> n;
    string s; cin >> s;

    vector<int> ans(n,0);
    char pile0 = 'a', pile1 = 'a';

    for(int i = 0; i < n; i++) {
        if(s[i] >= pile0 and s[i] >= pile1) {
            if(pile0 >= pile1) ans[i] = 0, pile0 = s[i];
            else ans[i] = 1, pile1 = s[i];
        }

        else if(s[i] >= pile0) ans[i] = 0, pile0 = s[i];
        else if(s[i] >= pile1) ans[i] = 1, pile1 = s[i]; 
        else {
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    for(auto x : ans) cout << x;
    cout << endl;

    return 0;
}

