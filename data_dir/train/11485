#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, k; 
string s;
char getDiff(char prev, char next) {
    char c;
    if (k == 2) {
        do {
            c = rand() % k + 'A';
        } while (c == prev);
    }
    else {
        do {
            c = rand() % k + 'A';
        } while (c == prev || c == next);
    }
    return c;
}

void ps(const string& s) {
    cout << s.substr(1,n) << '\n';
}

int countDiff(string& a, string& b) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) res++;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n >> k >> s;
    if (k == 2) {
        string c1;
        for (int i = 0; i < n; i++) {
            c1 += (i % 2 == 0) ? 'A' : 'B';
        }
        string c2;
        for (int i = 0; i < n; i++) {
            c2 += (i % 2 == 0) ? 'B' : 'A';
        }
        if (countDiff(c1,s) < countDiff(c2,s)) {
            cout << countDiff(c1,s) << '\n';
            cout << c1 << '\n';
        }
        else {
            cout << countDiff(c2,s) << '\n';
            cout << c2 << '\n';
        }
    }
    else {
        s = '#' + s + '#';
        int ans = 0;
        for (int i = 2; i <= n; i++) {
            if (s[i] == s[i-1]) {
                s[i] = getDiff(s[i-1],s[i+1]);
                ans++;
            }
        }
        cout << ans << '\n';
        ps(s);
    }


    return 0;
}

