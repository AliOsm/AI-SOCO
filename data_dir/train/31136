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

const int T = 1e6 + 5;
int v[T];
int in[30];
int out[30];
int n,k;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> k >> s;
    memset(in, INF, sizeof in);

    for(int i = 0; i < n; i++) {
        in[s[i]-'A'] = min(in[s[i]-'A'], i+1);
        out[s[i]-'A'] = max(out[s[i]-'A'], i+1);
    }

    for(int i = 0; i < 30; i++)
        if(out[i]) v[in[i]]++, v[out[i]+1]--;

    for(int i = 1; i < T; i++) {
        v[i] += v[i-1];
        if(v[i] > k) { cout << "YES" << endl; return 0; }
    }

    cout << "NO" << endl;
    return 0;
}

