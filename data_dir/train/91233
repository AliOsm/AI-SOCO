#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int loss(string a, string b) {
    int res = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) res++;
    }
    return res;
}

string getr(int r, int g, int b, int n) {
    string ret(n,'#');
    for (int i = r; i < n; i += 3) ret[i] = 'R';
    for (int i = g; i < n; i += 3) ret[i] = 'G';
    for (int i = b; i < n; i += 3) ret[i] = 'B';
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n; cin >> n;
    string s; cin >> s;
    pair<int,string> ans = {999999,""};
    vector<int> perm = {0,1,2};
    do {
        string t = getr(perm[0],perm[1],perm[2],n);
        ans = min(ans,{loss(t,s),t});
    } while (next_permutation(perm.begin(),perm.end()));
    cout << ans.first << '\n' << ans.second << '\n';


    return 0;
}

