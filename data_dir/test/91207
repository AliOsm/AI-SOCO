#include <iostream>
#include <vector>

#define MAXN 1000006

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int min_ones = n - 1;
    int max_ones = 2 * (n + 1);
    if (m < min_ones || m > max_ones) {
        cout << -1 << '\n';
    } else if (m == min_ones) {
        for (int i = 0; i < (n - 1); ++i) {
            cout << "01";        
        }
        cout << "0\n";
    } else {
        vector<int> group_size;

        for (int i = 0; i < n; ++i) {
            group_size.push_back(1);
            m--;
        }

        for (int i = 0; m > 0 && i < n; ++i) {
            group_size[i] += 1;
            m--;
        }

        if (m > 0) {
            group_size.push_back(m);
        }

        /*
        for (int i = 0; i < (int)group_size.size(); ++i) {
            cout << group_size[i] << ' ';
        }
        cout << '\n';
        */
        for (int i = 0; i < group_size[0]; ++i) {
            cout << '1';
        }

        for (int i = 1; i < n; ++i) {
            cout << '0' << (group_size[i] == 1 ? "1" : "11");
        }
        cout << '0';

        if (group_size.size() > n) {
            cout << (group_size[n] == 1 ? "1" : "11");
        }
    }

    cout << '\n';
    return 0;
}
