#include<bits/stdc++.h>
using namespace std;
int a[12345];
vector<pair<int, int> > v;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int n,k;
    cin >> n >> k;
    for(int i = 1; i <= n; i++){
            int x;
    cin >> x;
        v.push_back(make_pair(x, i));
    }
    sort(v.rbegin(), v.rend());
    int ans = 0;
    for(int i = 0; i < k; i++){
        ans += v[i].first;
        a[i] = v[i].second;
    }
    a[k] = 0;
    sort(a, a+k+1);
cout<<ans<<endl;
    for(int i = 0; i < k ; i++){
            //cout<<a[i]<<"  ";//<<endl;
        int p  = a[i+1] - a[i];
        if(i == k - 1)p += n - a[i+1];
        cout<<p<<" ";
    }
    return 0;
}
