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
    ios::sync_with_stdio(false);
    string s; cin >> s;
    int n; cin >> n;
    
    int mini = 0;
    int maxi = 0;
    int ok = 0;

    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '?') mini--;
        else if(s[i] == '*') maxi += 200, mini--;
        else maxi++, mini++, ok++;
    }
    
    s += '#';

    if(n >= mini and n <= maxi) {
        for(int i = 0; i < s.size()-1; i++) {
            while((n > ok) and s[i+1] == '*') {
                ok++;
                cout << s[i];
            }
            if((n < ok) and (s[i+1] == '*' or s[i+1] == '?')) {
                ok--;
                continue;
            }
            if(s[i] != '*' and s[i] != '?') cout << s[i];
        }
        cout << endl;
    } else cout << "Impossible" << endl;
    

    return 0;
}

