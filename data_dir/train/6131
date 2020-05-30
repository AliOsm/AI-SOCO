#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;

    cin >> T;

    while(T--) {
        int n,k;
        cin >> n >> k;

        bool win = false;

        if(k % 3 != 0) {
            if(n % 3 == 0)
                win = false;
            else
                win = true;
        }
        else {
            int m = n % (k+1);
            if(m % 3 == 0 && m != k)
                win = false;
            else
                win = true;
        }

        cout << (win ? "Alice" : "Bob") << endl;
    }

    return 0;
}
