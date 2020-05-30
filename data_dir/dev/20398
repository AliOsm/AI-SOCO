#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define sec second

typedef long long ll;
const int INF = 0x3f3f3f3f;

int main() {
    ios::sync_with_stdio(false);
    map<char,int>ind;
    int n; cin >> n;
    string s; cin >> s;
    for(int i = 0; i < s.size(); i++) {
        ind[s[i]]++;
    }
    for(auto id : ind) {
        if(id.sec % n != 0) { cout << -1 << endl; return 0; }
    }

    for(int i = 0; i < n; i++) { 
        for(auto id : ind) { 
            for(int i = 0; i < id.sec / n; i++) cout << id.fi;
        }
    }
    cout << endl;

    return 0;
}

