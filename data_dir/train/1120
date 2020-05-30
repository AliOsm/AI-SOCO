#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int maxn = 105;
int n, x, y;
int a[maxn];

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n >> x >> y;
    priority_queue<int,vector<int>,greater<int>> q;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        q.push(a[i]);    
    }
    if (x > y) {
        cout << n << '\n';
        return 0;
    }
    else {
        int cnt = 0;
        while (!q.empty() && q.top() <= x) {
            cnt++;
            q.pop();
            if (!q.empty()) {
                int t = q.top(); q.pop();
                q.push(t+y);    
            }
        }
        cout << cnt << '\n';
    }


    return 0;
}

