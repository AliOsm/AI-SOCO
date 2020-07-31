#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int n;
int t[5005];
int freq[5005];
int ans[5005];

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) 
        cin >> t[i];

    for (int start = 0; start < n; ++start) {
        memset(freq, 0, sizeof(freq));
        freq[t[start]]++;

        int largest = t[start];
        ans[largest]++;
        for (int end = start + 2; end <= n; ++end) {
            freq[t[end - 1]]++;
            if (freq[t[end - 1]] > freq[largest] or (freq[t[end - 1]] == freq[largest] and t[end - 1] < largest)) {
                largest = t[end - 1];
            }

            ans[largest]++;
        }
    }

    cout << ans[1];
    for (int i = 2; i <= n; ++i) {
        cout << ' ' << ans[i];
    }
    cout << '\n';

    return 0;
}
