#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

bool ok[(int)1e6];
int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);

    string s;
    cin >> s;
    int n = (int)s.length();

    int mx = 1, cnt = 1;
    for(int i = 0; i < 2 * n; i++) {
        char nxt = s[(i + 1) % n];
        if(s[i % n] != nxt) cnt++;
        else cnt = 1;
        mx = max(mx, cnt);
    }
    cout << min(mx, n) << "\n";
}