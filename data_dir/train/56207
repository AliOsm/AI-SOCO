#include <bits/stdc++.h>
#include <bitset>

typedef long long ll;

using namespace std;

const int n_=1e6+10;
int n;
char s[n_];
int z[n_];
bool can_suf[n_];
bool can_bet[n_];
void compute_z() {
    int L = -1, R = -1;
    z[0] = n;
    for(int i = 1; i < n; i++) {
        if(i > R) {
            L = R = i;
            while(R < n && s[R] == s[R - L]) R++;
            z[i] = R - L;
            R--;
        } else {
            int k = i - L;
            if(z[k] < R - i + 1) {
                z[i] = z[k];
            } else {
                L = i;
                while(R < n && s[R] == s[R - L]) R++;
                z[i] = R - L;
                R--;
            }
        }
    }
}

int main() {
    scanf("%s", s);
    n = strlen(s);
    compute_z();
    for(int i = 1; i < n; i++) {
        if(z[i] == n - i) {
            can_suf[n - i] = 1;
        }
        can_bet[min(n - i - 1, z[i])] = 1;
    }
    int len = -1, last_suff = -1;
    for(int i = 1; i <= n; i++) {
        if(can_suf[i]) {
            last_suff = i;
        }
        if(can_bet[i]) {
            if(len < last_suff) {
                len = last_suff;
            }
        }
    }

    if(len == -1) {
        printf("Just a legend\n");
    } else {
        string ss = string(s);
        printf("%s\n", ss.substr(0, len).c_str());
    }
}