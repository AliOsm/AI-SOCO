#include <iostream>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;

int NORTH = 0;
int EAST = 1;
int SOUTH = 2;
int WEST = 3;

int main() {
    int n;
    cin >> n;
    // 0 - left turn, 1 - right turn
    vector<int> turns;
    int x1, y1, x2, y2;
    cin >> x1 >> y1;
    int d = NORTH;
    for (int i = 0; i < n; ++i) {
        cin >> x2 >> y2;
        if (x1 < x2 and y1 == y2) {
            turns.push_back(d == NORTH);
            d = EAST;
        } else if (x1 > x2 and y1 == y2) {
            turns.push_back(d == SOUTH);
            d = WEST;
        } else if (x1 == x2 and y1 < y2) {
            turns.push_back(d == WEST);
            d = NORTH;
        } else if (x1 == x2 and y1 > y2) {
            turns.push_back(d == EAST);
            d = SOUTH;
        }
        x1 = x2;
        y1 = y2;
    }
    turns.erase(turns.begin());

    /*
    cout << turns[0];
    for (int i = 1; i < n; ++i) {
        cout << ' ' << turns[i];
    }
    cout << '\n';
    */

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (!turns[i])
            ++ans;
    }

    cout << ans << '\n';

    return 0;
}
