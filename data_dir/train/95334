#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    set<int> s;
    vector<int> sep;
    for (int i = 1, a; i <= n; i++) {
        scanf("%d", &a);
        if (s.count(a)) {
            sep.push_back(i);
            s.clear();
        } else {
            s.insert(a);
        }
    }
    if (sep.empty()) {
        puts("-1");
    } else if (sep.size() == 1) {
        printf("1\n1 %d\n", n);
    } else {
        printf("%d\n", sep.size());
        printf("1 %d\n", sep[0]);
        for (int i = 1; i < sep.size() - 1; i++)
            printf("%d %d\n", sep[i-1] + 1, sep[i]);
        printf("%d %d\n", sep[sep.size()-2] + 1, n);
    }

    return 0;
}
