#include <cstdio>
#include <cassert>
#include <set>

using namespace std;

set<int> full_left;
set<int> full_right;

set<int> values;
set<int> neg_values;

int main() {
    int n;
    scanf("%d", &n);

    int x;
    scanf("%d", &x);

    values.insert(x);
    neg_values.insert(-x);

    for (int i = 1; i < n; ++i) {
        scanf("%d", &x);
        // handle the edge cases
        if (x < *values.begin()) {
            full_left.insert(*values.begin());
            printf("%d ", *values.begin());
        } else if (x > *values.rbegin()) {
            full_right.insert(*values.rbegin());
            printf("%d ", *values.rbegin());
        } else {
            // find the nodes surrounding x
            int lower = -1 * (*neg_values.upper_bound(-x));
            int upper = *values.upper_bound(x);
            
            // printf("%d %d %d\n", lower, x, upper);
            assert(full_right.count(lower) ^ full_left.count(upper));
            if (full_right.find(lower) == full_right.end()) {
                full_right.insert(lower);
                printf("%d ", lower);
            } else {
                full_left.insert(upper);
                printf("%d ", upper);
            }
        }

        values.insert(x);
        neg_values.insert(-x);
    }
}
