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

int slow[26];
int sup[26];
int tlow[26];
int tup[26];

int main() {
    ios::sync_with_stdio(false);
    string s, t; cin >> s >> t;
    int a = 0; int b = 0;

    for(int i = 0; i < s.size(); i++) {
        if(s[i] < 'a') sup[s[i]-'A']++;
        else slow[s[i]-'a']++;
    }
    for(int i = 0; i < t.size(); i++) {
        if(t[i] < 'a') tup[t[i]-'A']++;
        else tlow[t[i]-'a']++;
    }

    int x;
    for(int i = 0; i < 26; i++) {
        if(slow[i] and tlow[i]) {
            x = min(slow[i], tlow[i]);
            a += x;
            slow[i] -= x;
            tlow[i] -= x;
        }

        if(sup[i] and tup[i]) {
            x = min(sup[i], tup[i]);
            a += x;
            sup[i] -= x;
            tup[i] -= x;
        }

        slow[i] += sup[i];
        tlow[i] += tup[i];

        if(slow[i] and tlow[i]) {
            x = min(slow[i], tlow[i]);
            b += x;
        }
    }

    cout << a << " " << b << endl;
    

    return 0;
}

