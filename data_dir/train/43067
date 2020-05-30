#include <bits/stdc++.h>
using namespace std;

#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int T = 5e5 + 3;
int v[T][30];

int main() {
    ios_base::sync_with_stdio(false);
    string s;
    cin >> s;
    s = "#" + s;

    for(int i = 1; i < s.size(); i++) v[i][s[i]-'a'+1]++;

    for(int i = 1; i < s.size(); i++)
        for(int j = 0; j < 30; j++)
            v[i][j] += v[i-1][j];

    for(int i = 1; i < s.size(); i++)
        for(int j = 1; j < 30; j++)
            v[i][j] += v[i][j-1];

    for(int i = 1; i < s.size(); i++)
        cout << ((v[i-1][s[i]-'a'])? "Ann" : "Mike") << endl;

    return 0;
}

