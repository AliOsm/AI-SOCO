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

int main() {
    ios_base::sync_with_stdio(false);
    string s; cin >> s;

    int close = s.size()-1;
    int open = s.size()-1;
    int ans = 0;

    while(open >= 0) {
        while(close >= 0 and s[close] == '(') close--;
        open = min(close,open);
        while(open >= 0 and s[open] == ')') open--;

        if(close == -1 or open == -1) break;
        //cout << open << " " << close << endl;

        close--;
        open--;
        ans += 2;
    }

    cout << ans << endl;

    return 0;
}

