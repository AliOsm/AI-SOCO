#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int calc(vector<int> v)
{
    sort(v.begin(), v.end());
    int ans = 0;
    for(int i = 1; i < int(v.size()); i+=2)
    {
        ans += v[i]-v[i-1];
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    cin>>n;
    vector<int> v;
    for(int i = 0; i < n; ++i)
    {
        int a, b;
        cin>>a>>b;
        v.push_back(a);
        v.push_back(b);
    }
    int ans = 1e9;
    for(int i = 0; i < 2*n; ++i)
    {
        for(int j = i+1; j < 2*n; ++j)
        {
            vector<int> t;
            for(int k = 0; k < 2*n; ++k)
                if(i!=k && j!=k)
                    t.push_back(v[k]);
            ans = min(calc(t), ans);
        }
    }
    cout<<ans<<endl;
    return 0;
}
