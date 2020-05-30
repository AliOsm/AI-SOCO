#include<bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 5;
int cnt[maxn];
int main()
{
    int n, k;
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        cnt[x%k]++;
    }
    int ans = 0;
    for(int i = 0; i < n; i++){
            if(i > k - i)continue;
        if(i == 0) ans += cnt[i]/2;
        else if(i == k - i) ans += cnt[i]/2;
        else{
            ans += min(cnt[i], cnt[k - i]);
        }
    }
    cout << ans*2 << endl;
    return 0;
}
