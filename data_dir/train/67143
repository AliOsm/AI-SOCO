#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;

    cin >> n;

    int even = 0 , odd = 0;
    int g = 1;

    for(int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        g = __gcd(g,x);
        odd += (x&1);
        even += !(x&1);
    }

    if(g % 2 == 0)
        cout << 0 << endl;
    else
        cout << min(even,odd) << endl;

    return 0;
}
