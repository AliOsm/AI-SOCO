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

const int T = 105;
int dp[T][3][10][2];
int choose[T][3][10][2];
string s;
int n;
bool flag;

int f(int at, int casa, int rest) {
    int x = s[at] - '0';
    x *= max(1,10 * casa);
    x += rest;
    return x % 8;
}

int solve(int at, int casa, int rest, bool ok) {
    if(ok and !rest) return 0;
    if(at == n or casa > 2) return (ok and !rest? 0 : -INF);

    if(dp[at][casa][rest][ok] != -1) return dp[at][casa][rest][ok];

    if(s[at] == '0') flag = true;

    int L,R = -INF;

    L = solve(at+1, casa, rest, ok);
    if((s[at] == '0' and ok)  or s[at] != '0') R = solve(at+1, casa+1, f(at, casa, rest) , 1) + 1; 

    if(R > L) choose[at][casa][rest][ok] = 1;
    return dp[at][casa][rest][ok] = max(R,L);
}

void build(int at, int casa, int rest, bool ok) {
    if(ok and !rest) return;
    if(at == n or casa > 2) return;
    if(choose[at][casa][rest][ok]) {
        build(at+1, casa+1, f(at,casa,rest), 1);
        cout << s[at];
    } else {
        build(at+1, casa, rest, ok);
    }
}
        


int main() {
    ios::sync_with_stdio(false);
    memset(dp, -1, sizeof dp);

    cin >> s;
    reverse(s.begin(), s.end());
    n = s.size();

    int x = solve(0,0,0,0);

    if(x > 0) cout << "YES" << endl, build(0,0,0,0), cout << endl;
    else if(flag) cout << "YES" << endl << 0 << endl;
    else cout << "NO" << endl;

    return 0;
}

