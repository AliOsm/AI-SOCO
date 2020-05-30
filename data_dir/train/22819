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

    if(n == 1 || n == 2) {
        cout << "No\n";
        return 0;
    }
    vector<int> a, b;
    for(int i = 1; i <= n; i++) {
        if(i & 1) {
            a.push_back(i);
        } else {
            b.push_back(i);
        }
    }
    if(ok(a, b)) {
        print(a, b);
        return 0;
    }
    a = vector<int>();
    b = vector<int>();
    a.push_back(1);
    a.push_back(2);
    for(int i = 3; i <= n; i++) {
        b.push_back(i);
    }
    if(ok(a, b)) {
        print(a, b);
        return 0;
    }
    cout << "No\n";
    return 0;
}