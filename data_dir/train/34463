#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool ok(vector<int> a, vector<int> b) {
    ll sum = 0;
    for(int i : a) sum += i;
    ll sum2 = 0;
    for(int i : b) sum2 += i;
    return __gcd(sum ,sum2) > 1;
}

void print (vector<int> a, vector<int> b) {
    cout << "Yes\n";
    int sz1 = (int)a.size();
    cout << sz1;
    for(int i = 0; i < sz1; i++) {
        cout << " " << a[i];
    }
    cout << "\n";

    int sz2 = (int)b.size();
    cout << sz2 ;
    for(int i = 0; i < sz2; i++) {
        cout << " " << b[i];
    }
    cout << "\n";
    return;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for(int i = 0; i < n; i++) {
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i1 = n - 1, i2 = n - 1;
    int p = 0;
    ll diff = 0;
    while(i1 >= 0 || i2 >= 0) {
        if(!p) {
            if(i1 >= 0 && i2 >= 0) {
                if(a[i1] > b[i2]) {
                    diff += a[i1];
                    i1--;
                } else {
                    i2--;
                }
            } else if(i1 >= 0) {
                diff += a[i1];
                i1--;
            } else {
                i2--;
            }
        } else {

            if(i1 >= 0 && i2 >= 0) {
                if(a[i1] < b[i2]) {
                    diff -= b[i2];
                    i2--;
                } else {
                    i1--;
                }
            } else if(i1 >= 0) {
                i1--;
            } else {
                diff -= b[i2];
                i2--;
            }
        }
        p ^= 1;
    }
    cout << diff << "\n";
    return 0;
}