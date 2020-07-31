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

vector<string> ans;

bool cmp(const string &a, const string &b) {
    return (a+b < b+a);
}

int main() {
    ios::sync_with_stdio(false);
    int n; cin >> n;
    string s;
    int maxi = 0;
    for(int i = 0; i < n; i++) {
        cin >> s;
        ans.pb(s);
    }

    sort(ans.begin(), ans.end(), cmp);

    for(auto x : ans)  cout << x;
    cout << endl;

    return 0;
}

