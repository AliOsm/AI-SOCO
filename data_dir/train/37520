#include <iostream>

using namespace std;

int solve(int a, int b) {
    int count = 0;
    while(a != 0 && b != 0) {
        if(a > b) {
            count += (a / b);
            a %= b;
        } else {
            count += (b / a);
            b %= a;
        }
    }
    return count;
}

int main() {
    int N, a, b;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        cout << solve(a, b) << '\n';
    }
    return 0;
}
