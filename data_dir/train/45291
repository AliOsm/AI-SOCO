#include <bits/stdc++.h>

using namespace std;

typedef long long ll;



int main() {
    int n, m, side;
    cin >> n >> m;
    vector<string> v(n), c(m);
    for(int i = 0; i < n; i++) {
        cin >> v[i];
        if(v[i].find("B") != -1) {
            side++;
        }
        for(int j = 0; j < m; j++) {
            c[j] += v[i][j];
        }
    }
    side /= 2;
    int tmp = side;
    int r = -1, col = -1;
    for(int i = 0; i < n; i++) {
        if(v[i].find("B") != -1) {
            side--;
            if(!side) {
                r = i;
                break;
            }
        }
    }
    for(int i = 0; i < m; i++) {
        if(c[i].find("B") != -1) {
            tmp--;
            if(!tmp) {
                col = i;
                break;
            }
        }
    }
    cout << r + 1 << " " << col + 1 << "\n";
}